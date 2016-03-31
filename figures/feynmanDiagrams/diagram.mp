% diagram.mp -- do not edit, generated automatically by feynmanDiagrams.tex
input feynmp
require_RCS_revision "1.30";
beginchar(1, 200*1.0pt#,  80*1.0pt#, 0);
"feynmf: 1";
LaTeX_unitlength:=1.0pt;
subgraph (0, 0, w, h);
vinit;
pickup pencircle scaled thin;
vleft (__i1, __i2);
vright (__o1, __o2, __o3, __o4);
vconnect ("gluon", __i1, __v1);
vconnect ("fermion", __o1, __v1);
vconnect ("gluon", __i2, __v4);
vconnect ("fermion", __v4, __o4);
vfreeze;
vconnect ("fermion", __v1, __v2);
vconnect ("gluon", __v2, __v3);
vconnect ("fermion", __v3, __v4);
vfreeze;
vconnect ("fermion", __o3, __v3);
vconnect ("fermion", __v2, __o2);
vfreeze;
vdraw;
endsubgraph;
endchar;
% the end.
end.
endinput;
