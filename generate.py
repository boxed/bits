from PIL import Image

h = 2_000_000
w = 19
img = None
pixels = None
c = 0

for y in range(h):
    if y % 20_000 == 0:
        if img is not None:
            img = img.convert('P')
            img.save(f'{c}.png')
            print(f'<img src="{c}.png" style="width: 400px; max-width: 100%; image-rendering: pixelated;">')
            c += 1

        img = Image.new(mode='RGB', size=(w, 20_000), color=0xFF_FF_FF)
        pixels = img.load()

    for x, b in enumerate(f'{y:b}'.zfill(w)):
        pixels[(x, y % 20_000)] = 0x00_00_00 if b == '0' else 0xFF_FF_00

