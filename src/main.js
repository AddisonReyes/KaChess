import kaplay from "kaplay";
import { addChessboard } from "./chessboard.js";

const TILE = 64;
const SQUARE_PAD = 32;
const W = 8 * TILE + 2 * SQUARE_PAD;
const H = 8 * TILE + 2 * SQUARE_PAD;

kaplay({
  width: W,
  height: H,
  background: "#292929",
});

addChessboard({
  tileSize: TILE,
  squarePad: SQUARE_PAD,
  borderPad: 30,
  light: [240, 240, 240],
  dark: [24, 24, 24],
  border: [240, 240, 240],
  layer: 0,
});
