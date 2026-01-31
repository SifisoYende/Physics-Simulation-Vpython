from vpython import box, sphere, vec, color, rate, attach_trail, arrow

# --- CONSTANTS ---
# Using uppercase for values that don't change makes code more readable
BOX_SIZE = 12
HALF_BOX = BOX_SIZE / 2
WALL_THICKNESS = 0.2
BALL_RADIUS = 0.5
TIME_STEP = 0.005
SIM_DURATION = 3  # seconds

class PhysicsSimulation:
    """
    Encapsulates the logic for a 3D bouncing ball simulation.
    Demonstrates separation of concerns and object-oriented design.
    """
    def __init__(self):
        # 1. Initialize Scene
        self.ball = sphere(pos=vec(-5,0,0), radius=BALL_RADIUS, color=color.cyan)
        self.ball.velocity = vec(25, 5, 15)
        
        # Visual debugging tools
        self.v_scale = 0.1
        self.v_arrow = arrow(pos=self.ball.pos, axis=self.v_scale * self.ball.velocity, color=color.yellow)
        attach_trail(self.ball, color=self.ball.color)
        
        self._build_walls()

    def _build_walls(self):
        """Private helper to set up the environment."""
        wall_color = color.green
        # Right, Left, Top, Bottom, Back
        box(pos=vec(HALF_BOX, 0, 0), size=vec(WALL_THICKNESS, BOX_SIZE, BOX_SIZE), color=wall_color)
        box(pos=vec(-HALF_BOX, 0, 0), size=vec(WALL_THICKNESS, BOX_SIZE, BOX_SIZE), color=wall_color)
        box(pos=vec(0, HALF_BOX, 0), size=vec(BOX_SIZE, WALL_THICKNESS, BOX_SIZE), color=wall_color)
        box(pos=vec(0, -HALF_BOX, 0), size=vec(BOX_SIZE, WALL_THICKNESS, BOX_SIZE), color=wall_color)
        box(pos=vec(0, 0, -HALF_BOX), size=vec(BOX_SIZE, BOX_SIZE, WALL_THICKNESS), color=wall_color)

    def handle_collisions(self):
        """Logic to invert velocity when hitting boundaries."""
        # X-axis (Left/Right)
        if abs(self.ball.pos.x) + BALL_RADIUS > HALF_BOX:
            self.ball.velocity.x *= -1
            
        # Y-axis (Top/Bottom)
        if abs(self.ball.pos.y) + BALL_RADIUS > HALF_BOX:
            self.ball.velocity.y *= -1

        # Z-axis (Back/Front)
        if abs(self.ball.pos.z) + BALL_RADIUS > HALF_BOX:
            self.ball.velocity.z *= -1

    def update(self, dt):
        """State update for each frame."""
        self.handle_collisions()
        self.ball.pos += self.ball.velocity * dt
        
        # Update visual arrow
        self.v_arrow.pos = self.ball.pos
        self.v_arrow.axis = self.v_scale * self.ball.velocity

def run_simulation():
    """Main execution loop."""
    sim = PhysicsSimulation()
    t = 0
    while t < SIM_DURATION:
        rate(200)
        sim.update(TIME_STEP)
        t += TIME_STEP

if __name__ == "__main__":
    run_simulation()
