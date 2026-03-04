export function addChessboard(opts = {}) {
  const {
    tileSize = 64,
    squarePad = 32,
    borderPad = 30,
    light = [240, 240, 240],
    dark = [24, 24, 24],
    border = [240, 240, 240],
    layer = 0,
  } = opts;

  const boardSize = 8 * tileSize;
  const outerW = boardSize + (squarePad - borderPad) * 2;
  const outerH = boardSize + (squarePad - borderPad) * 2;

  add([
    rect(outerW, outerH),
    pos(borderPad, borderPad),
    color(border[0], border[1], border[2]),
    z(layer),
  ]);

  for (let row = 0; row < 8; row++) {
    for (let col = 0; col < 8; col++) {
      const isLight = (row + col) % 2 === 0;
      const c = isLight ? light : dark;

      add([
        rect(tileSize, tileSize),
        pos(squarePad + col * tileSize, squarePad + row * tileSize),
        color(c[0], c[1], c[2]),
        z(layer + 1),
      ]);
    }
  }
}
