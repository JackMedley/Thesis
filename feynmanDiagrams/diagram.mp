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
vright (__o1, __o2);
vconnect ("fermion, label=$p_b$,label.dist=.12h", __i1, __v1);
vconnect ("fermion", __v1, __v3);
vconnect ("fermion, label=$p_2$,label.dist=.12h", __v3, __o1);
vconnect ("fermion, label=$p_a$", __i2, __v2);
vconnect ("fermion", __v2, __v4);
vconnect ("fermion, label=$p_1$", __v4, __o2);
vfreeze;
vconnect ("gluon", __v2, __v1);
vconnect ("gluon", __v3, __v4);
vlabel ("$q$", __i2);
vlabel ("$g$", __i1);
vlabel ("$q$", __o2);
vlabel ("$g$", __o1);
vfreeze;
vdraw;
endsubgraph;
endchar;
% the end.
end.
endinput;
