const fs = require("fs");
const jpickle = require("jpickle");
const binary = fs.readFileSync("model.pkl", "binary");
const data = jpickle.loads(binary);
console.log(data);
