from dolfin import *
from mshr import *

# Create mesh and define function space
domain = Circle(Point(0, 0), 32)
mesh = generate_mesh(domain, 64)
#mesh = cpp.mesh.SphereMesh(Point(0.0, 0.0, 0.0), 10, 0.1)
V = FunctionSpace(mesh, "Lagrange", 1)

def boundary(x, on_boundary):
    return on_boundary

# Define boundary condition
u0 = Constant(0.0)
bc = DirichletBC(V, u0, boundary)

# Define variational problem
u = TrialFunction(V)
v = TestFunction(V)
f = Constant(6.0)
a = inner(grad(u), grad(v))*dx
L = f*v*dx

# Compute solution
u = Function(V)
solve(a == L, u, bc)

# Save solution in VTK format
file = File("poisson.pvd")
file << u

# Plot solution
import matplotlib.pyplot as plt
plot(u)
plt.show()
