/* رانتایم کوچک صفحه‌های تعاملی — همان معناشناسی قالب‌های اصلی پروژه:
   {{مسیر}}، <sc-for>، <sc-if> و هندلرهای رویداد، با نگهداری فوکوس ورودی‌ها. */
(function (w) {
  'use strict';

  function resolve(path, scopes) {
    var p = String(path).trim();
    if (p === 'true') return true;
    if (p === 'false') return false;
    if (p === 'null') return null;
    if (/^-?\d+(\.\d+)?$/.test(p)) return Number(p);
    var bits = p.split('.');
    for (var i = scopes.length - 1; i >= 0; i--) {
      var s = scopes[i];
      if (s && Object.prototype.hasOwnProperty.call(s, bits[0])) {
        var v = s[bits[0]];
        for (var j = 1; j < bits.length && v != null; j++) v = v[bits[j]];
        return v;
      }
    }
    return undefined;
  }

  function str(v) { return v == null || v === false ? '' : String(v); }

  function attrValue(v, scopes) {
    if (v === null) return null;
    if (typeof v === 'string') return v;
    if (v.h !== undefined) return resolve(v.h, scopes);
    var out = '';
    for (var i = 0; i < v.p.length; i++) {
      var x = v.p[i];
      out += typeof x === 'string' ? x : str(resolve(x.h, scopes));
    }
    return out;
  }

  var SVG = 'http://www.w3.org/2000/svg';

  function build(ast, scopes, frag, svg) {
    for (var n = 0; n < ast.length; n++) {
      var node = ast[n];
      if (typeof node === 'string') { frag.appendChild(document.createTextNode(node)); continue; }
      if (node.h !== undefined) {
        frag.appendChild(document.createTextNode(str(resolve(node.h, scopes))));
        continue;
      }
      if (node.f !== undefined) {
        var list = resolve(node.f, scopes) || [];
        for (var i = 0; i < list.length; i++) {
          var scope = {};
          scope[node.as] = list[i];
          scope.$index = i;
          build(node.k || [], scopes.concat([scope]), frag, svg);
        }
        continue;
      }
      if (node.i !== undefined) {
        if (resolve(node.i, scopes)) build(node.k || [], scopes, frag, svg);
        continue;
      }

      var inSvg = svg || node.n === 'svg';
      var el = inSvg ? document.createElementNS(SVG, node.n) : document.createElement(node.n);
      if (node.c) el.setAttribute('class', node.c);
      var pendingValue = null;
      for (var key in node.a || {}) {
        var v = attrValue(node.a[key], scopes);
        if (v === null || v === undefined || typeof v === 'function') {
          if (node.a[key] === null) el.setAttribute(key, '');
          continue;
        }
        if (key === 'value' && (node.n === 'input' || node.n === 'select' || node.n === 'textarea')) {
          pendingValue = String(v);
          if (node.n === 'input') el.setAttribute('value', pendingValue);
          continue;
        }
        if (key === 'class' && node.c) { el.setAttribute('class', node.c + ' ' + v); continue; }
        el.setAttribute(key, String(v));
      }
      for (var ev in node.e || {}) {
        var fn = resolve(node.e[ev], scopes);
        if (typeof fn === 'function') el.addEventListener(ev, fn);
      }
      if (node.r) el.textContent = (node.k || []).join('');
      else if (node.k) build(node.k, scopes, el, inSvg);
      if (pendingValue !== null) el.value = pendingValue;
      frag.appendChild(el);
    }
  }

  function DCLogic(props) { this.props = props || {}; this.state = {}; }
  DCLogic.prototype.setState = function (patch) {
    var next = typeof patch === 'function' ? patch(this.state, this.props) : patch;
    for (var k in next) this.state[k] = next[k];
    this._render();
  };
  DCLogic.prototype.forceUpdate = function () { this._render(); };
  DCLogic.prototype._render = function () {
    var host = this._host;
    var active = document.activeElement;
    var keep = active && active.id && host.contains(active)
      ? { id: active.id, s: active.selectionStart, e: active.selectionEnd, scroll: w.scrollY }
      : null;
    var frag = document.createDocumentFragment();
    build(this._ast, [this.renderVals()], frag, false);
    host.textContent = '';
    host.appendChild(frag);
    if (keep) {
      var again = document.getElementById(keep.id);
      if (again) {
        again.focus({ preventScroll: true });
        try { again.setSelectionRange(keep.s, keep.e); } catch (err) { /* number/select */ }
        if (w.scrollY !== keep.scroll) w.scrollTo(0, keep.scroll);
      }
    }
  };

  w.DCLogic = DCLogic;
  w.dcMount = function (ast, Component) {
    var host = document.getElementById('dc-root');
    if (!host) return;
    var c = new Component({});
    c._ast = ast;
    c._host = host;
    c._render();
    // تخته‌هایی که به‌جای حفره‌های {{...}} مستقیم با DOM کار می‌کنند، کارشان را
    // این‌جا شروع می‌کنند؛ بعد از اینکه نخستین رندر در صفحه نشست.
    if (typeof c.componentDidMount === 'function') c.componentDidMount();
  };
})(window);
