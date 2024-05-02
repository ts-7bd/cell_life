import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
GREY = (180, 180, 180)
YELLOW = (255, 255, 0)

WIDTH, HEIGHT = 900, 600
TILE_SIZE = 10
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 120

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

def generate_cells(cells_per_row):
  # randomly generated positions are transformed to a set to avoid duplicates
  positions = [(random.randrange(0,GRID_WIDTH), random.randrange(0,GRID_HEIGHT)) for _i in range(cells_per_row)]
  print("cells", len(positions), len(set(positions)))
  return set(positions)

def adjust_grid(positions):
  all_neighbours = set()
  new_positions = set()

  for position in positions:
    neighbours = get_neighbours(position)
    all_neighbours.update(neighbours)

    neighbours = list(filter(lambda x: x in positions, neighbours))

    if len(neighbours) in [2, 3]:
      new_positions.add(position)

  for position in all_neighbours:
    neighbours = get_neighbours(position)
    neighbours = list(filter(lambda x: x in positions, neighbours))

    if len(neighbours) == 3:
      new_positions.add(position)
  
  return new_positions


def get_neighbours(position):
  x, y = position
  neighbours = []

  for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
      if x + dx in [-1, GRID_WIDTH + 1] or y + dy in [-1, GRID_HEIGHT + 1]:
        continue
      if dx == 0 and dy == 0:
        continue

      neighbours.append((x + dx, y + dy))
  
  return neighbours


def draw_grid(positions):

  for position in positions:
      col, row = position
      top_left = (col*TILE_SIZE, row*TILE_SIZE)
      pygame.draw.rect(screen, YELLOW, (*top_left, TILE_SIZE, TILE_SIZE))

  for row in range(GRID_HEIGHT):
    pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))

  for col in range(GRID_WIDTH):
    pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))


def main():
  running = True
  playing = False
  count = 0
  update_freq = 60

  positions = set()
  positions.add((10,10))

  while running:
    clock.tick(60)

    if playing:
      count += 1

    if count >= update_freq:
      count = 0
      positions = adjust_grid(positions)

    pygame.display.set_caption("Playing" if playing else "Paused")

    for event in pygame.event.get():
      # print("event-type", event)

      if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        running = False
      
      if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        col = x // TILE_SIZE
        row = y // TILE_SIZE
        print("mouse click:", x, y, col, row)
        pos = (col, row)

        if pos in positions:
          positions.remove(pos)
        else:
          positions.add(pos)
        
      if event.type == pygame.KEYDOWN:
        print("event keydown:", event.type, event.key)

        if event.key == pygame.K_SPACE:
          playing = not playing
        
        if event.key == pygame.K_c:
          positions = set()
          playing = False
          count = 0
          
        if event.key == pygame.K_g:
          print("event press g: ", event.type, event.key)
          cells_per_row = random.randrange(15, 30)*GRID_WIDTH
          positions = generate_cells(cells_per_row)

    screen.fill(GREY)
    draw_grid(positions)
    pygame.display.update()
  
  
  pygame.quit()

# ensures that the main function is only called when it is run in the main file directly
if __name__ == "__main__":
  main()



