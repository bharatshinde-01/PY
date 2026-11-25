"""
REALISTIC ASCII / SCANLINE EYE
Made by Bharat

Install:
    pip install pygame numpy

Run:
    python bharat_eye.py

Controls:
    Move mouse  : eye follows your cursor
    SPACE       : blink
    R           : restart animation
    ESC / close : quit
"""

import math
import random
import sys
import pygame
import numpy as np

pygame.init()

W, H = 1100, 680
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("A HUMAN EYE  |  MADE BY BHARAT")
clock = pygame.time.Clock()

FONT = pygame.font.SysFont("consolas", 13)
BIG = pygame.font.SysFont("consolas", 58, bold=True)
SMALL = pygame.font.SysFont("consolas", 18, bold=True)

BG = (5, 5, 9)
PINK = (226, 91, 145)
WHITE = (225, 220, 211)

# ---------- Background: dark digital field ----------
random.seed(18)
stars = [(random.randrange(W), random.randrange(H),
          random.uniform(.25, 1.0), random.randrange(1, 3))
         for _ in range(180)]
glyphs = "01:;.*+░▒▓"

def draw_background(t):
    screen.fill(BG)
    for x, y, speed, size in stars:
        yy = (y + int(t * 18 * speed)) % H
        a = int(45 + 65 * speed)
        pygame.draw.circle(screen, (a//2, a//2, a), (x, yy), size)
    for i in range(75):
        x = (i * 137 + int(t * 9)) % W
        y = (i * 71) % H
        ch = random.Random(i).choice(glyphs)
        col = (35, 42, 53)
        screen.blit(FONT.render(ch, True, col), (x, y))
    # Subtle frame
    pygame.draw.rect(screen, (38, 39, 50), (22, 22, W-44, H-44), 1)

# ---------- Eye geometry ----------
CX, CY = W//2, H//2 - 12
EW, EH = 430, 205

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

def eye_opening(x, y, openness):
    # Almond-shaped opening with a soft vertical aperture
    half = EW * .5
    nx = x / half
    if abs(nx) >= 1:
        return False
    edge = math.sqrt(max(0.0, 1 - nx*nx))
    top = -EH * .5 * edge * openness
    bottom = EH * .5 * edge * openness
    return top <= y <= bottom

def make_eye_surface(t, mouse, blink):
    surf = pygame.Surface((W, H), pygame.SRCALPHA)
    # Surrounding skin / orbital shadow
    pygame.draw.ellipse(surf, (30, 17, 18, 255),
                        (CX-EW//2-35, CY-EH//2-44, EW+70, EH+88))
    pygame.draw.ellipse(surf, (73, 39, 35, 255),
                        (CX-EW//2-17, CY-EH//2-27, EW+34, EH+54), 12)
    pygame.draw.ellipse(surf, (16, 12, 15, 255),
                        (CX-EW//2-5, CY-EH//2-13, EW+10, EH+26), 7)

    openness = max(.025, 1.0 - blink)
    # White of eye clipped to almond shape
    sclera = pygame.Surface((EW+4, EH+4), pygame.SRCALPHA)
    for yy in range(EH+4):
        y = yy - (EH+4)/2
        for xx in range(EW+4):
            x = xx - (EW+4)/2
            if eye_opening(x, y, openness):
                edge = abs(y) / (EH*.5*max(openness,.05))
                shade = int(235 - 42*edge)
                # warm corners
                corner = abs(x)/(EW*.5)
                red = min(255, shade + int(12*corner))
                sclera.set_at((xx, yy), (red, shade-2, shade-5, 255))
    surf.blit(sclera, (CX-(EW+4)//2, CY-(EH+4)//2))

    # Iris tracks mouse with restrained movement
    mx, my = mouse
    dx = clamp((mx-CX)/360, -1, 1) * 29
    dy = clamp((my-CY)/260, -1, 1) * 16
    ix, iy = int(CX+dx), int(CY+dy)

    # Iris only while eye is open
    iris_r = int(91 * (0.25 + .75*openness))
    pygame.draw.circle(surf, (48, 24, 17, 255), (ix, iy), iris_r+7)
    pygame.draw.circle(surf, (143, 69, 30, 255), (ix, iy), iris_r)
    pygame.draw.circle(surf, (196, 123, 48, 255), (ix, iy), int(iris_r*.83))
    pygame.draw.circle(surf, (105, 48, 23, 255), (ix, iy), int(iris_r*.69), 4)

    # Radial iris fibres
    for k in range(150):
        a = k * math.tau / 150 + .035*math.sin(t*1.3+k)
        r1 = iris_r*.39
        r2 = iris_r*random.Random(k).uniform(.72, .96)
        x1, y1 = ix+math.cos(a)*r1, iy+math.sin(a)*r1
        x2, y2 = ix+math.cos(a)*r2, iy+math.sin(a)*r2
        c = (clamp(170+int(45*math.sin(k)), 0, 255),
             clamp(91+int(30*math.cos(k*2)), 0, 255), 35, 210)
        pygame.draw.line(surf, c, (x1,y1), (x2,y2), 1)

    # Pupil and glossy catchlights
    pupil_r = int(39 * (0.35 + .65*openness))
    pygame.draw.circle(surf, (3, 3, 5, 255), (ix, iy), pupil_r)
    pygame.draw.ellipse(surf, (255,255,245,235),
                        (ix-26, iy-38, 25, 14))
    pygame.draw.circle(surf, (255,255,255,180), (ix+25, iy+24), 7)

    # Upper and lower eyelid contours
    for k in range(4):
        col = (93-k*12, 49-k*7, 43-k*6, 255)
        rect = (CX-EW//2-3, CY-EH//2-10+k*5,
                EW+6, EH+20-k*10)
        pygame.draw.arc(surf, col, rect, math.pi, math.tau, 2)
        pygame.draw.arc(surf, col, rect, 0, math.pi, 2)

    # Eyelashes along upper lid
    for i in range(37):
        x = CX - EW//2 + 18 + i*(EW-36)/36
        nx = (x-CX)/(EW*.5)
        y = CY - EH*.5*math.sqrt(max(0,1-nx*nx))*openness
        length = 8 + 8*(1-abs(nx))
        pygame.draw.line(surf, (18, 11, 13, 255),
                         (int(x), int(y)), (int(x-3), int(y-length)), 2)

    # Fine scanlines create the reference's monitor / ASCII look
    for yy in range(CY-EH//2-30, CY+EH//2+31, 4):
        pygame.draw.line(surf, (5, 4, 7, 65),
                         (CX-EW//2-35, yy), (CX+EW//2+35, yy), 1)

    # Small veins in sclera
    for j in range(12):
        side = -1 if j % 2 == 0 else 1
        startx = CX + side*random.Random(j).uniform(125, 180)
        starty = CY + random.Random(j+30).uniform(-22, 22)
        endx = startx + side*random.Random(j+60).uniform(12, 38)
        endy = starty + random.Random(j+90).uniform(-13, 13)
        pygame.draw.line(surf, (160, 91, 88, 90),
                         (startx,starty), (endx,endy), 1)
    return surf

# ---------- ASCII-style text / credit animation ----------
def draw_credit(progress, t):
    overlay = pygame.Surface((W,H), pygame.SRCALPHA)
    overlay.fill((2, 2, 7, int(230*progress)))
    screen.blit(overlay, (0,0))

    title = "MADE BY"
    name = "BHARAT"
    # Particle reveal from scattered points into readable lettering
    for text, y, size in [(title, CY-55, 34), (name, CY+5, 86)]:
        font = pygame.font.SysFont("consolas", size, bold=True)
        mask = font.render(text, True, (255,255,255))
        mask_rect = mask.get_rect(center=(CX,y))
        points = []
        for yy in range(0, mask.get_height(), 3):
            for xx in range(0, mask.get_width(), 3):
                if mask.get_at((xx,yy)).a > 80:
                    points.append((mask_rect.x+xx, mask_rect.y+yy))
        for px, py in points:
            jitter = (1-progress)*random.Random(px*7+py*13).uniform(-95,95)
            xx = px + math.sin(t*2+py*.04)*jitter
            yy = py + math.cos(t*2+px*.03)*jitter
            glow = (255, 95, 157) if (int(px+py)%3) else (255, 205, 224)
            pygame.draw.circle(screen, glow, (int(xx),int(yy)), 1 if size<50 else 2)
    line = SMALL.render("THANK YOU FOR WATCHING", True, (190, 150, 170))
    screen.blit(line, line.get_rect(center=(CX, CY+105)))

# ---------- Main animation ----------
start = pygame.time.get_ticks()/1000
forced_blink = 0.0
auto_blink_at = 3.0
running = True

while running:
    dt = clock.tick(60)/1000
    now = pygame.time.get_ticks()/1000 - start
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                forced_blink = 1.0
            elif event.key == pygame.K_r:
                start = pygame.time.get_ticks()/1000
                auto_blink_at = 3.0

    # Blink pulse, plus automatic natural blinks
    if now >= auto_blink_at and now < 31:
        forced_blink = max(forced_blink, 1.0)
        auto_blink_at += random.uniform(3.2, 5.3)
    forced_blink = max(0.0, forced_blink - dt*4.2)
    blink = forced_blink**2

    draw_background(now)
    eye = make_eye_surface(now, mouse, blink)
    screen.blit(eye, (0,0))

    # Header and HUD
    header = SMALL.render("HUMAN EYE // LIVE TRACKING", True, (128, 132, 151))
    screen.blit(header, (42, 36))
    hint = FONT.render("MOVE CURSOR TO LOOK  |  SPACE: BLINK  |  R: RESTART", True, (85, 92, 110))
    screen.blit(hint, (42, H-43))

    # A brief final transition, then the requested signature stays on screen
    if now > 32:
        progress = clamp((now-32)/2.5, 0, 1)
        draw_credit(progress, now)

    pygame.display.flip()

pygame.quit()
sys.exit()
