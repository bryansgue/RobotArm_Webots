% scale(1000) import("fr07-h101.stl");

// Append pure shapes (cube, cylinder and sphere), e.g:
translate([0,27,0])
cube([44, 5, 26], center=true);
translate([-21,11,0])
cube([2, 27, 22], center=true);
translate([21,11,0])
cube([2, 27, 22], center=true);
// cylinder(r=10, h=10, center=true);
// sphere(10);
