from flask import Flask

app = Flask(__name__)

PAGE = r"""
<!DOCTYPE html>
<html lang="kk">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Оқу таймері</title>
<style>
  * { box-sizing: border-box; }
  body { font-family: Arial, sans-serif; margin: 0; min-height: 100vh; padding: 40px 16px; text-align: center;
         background: linear-gradient(135deg, #ffd1e8, #ff9ccc, #ffc4e1);
         background-size: 300% 300%; animation: bg 12s ease infinite; }
  @keyframes bg { 0%,100% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } }
  h1 { color: #fff; text-shadow: 0 3px 12px rgba(214,51,132,.6); margin-bottom: 24px; }
  .card { background: #fff; max-width: 380px; margin: 0 auto; padding: 24px; border-radius: 14px; }
  #time { font-size: 56px; font-weight: bold; color: #72243E; }
  .track { height: 10px; background: #F4C0D1; border-radius: 5px; margin: 16px 0; overflow: hidden; }
  #bar { height: 100%; width: 0; background: #993556; }
  #status { font-size: 14px; color: #5F5E5A; margin: 0 0 16px; }
  button { padding: 10px 16px; border-radius: 8px; border: 1px solid #993556; font-size: 15px; cursor: pointer;
           background: #fff; color: #72243E; margin: 0 4px; }
  button.main { background: #993556; color: #fff; }
  .count { font-size: 14px; margin-top: 18px; }
</style>
</head>
<body>
  <h1>Оқу таймері</h1>
  <div class="card">
    <div id="time">25:00</div>
    <div class="track"><div id="bar"></div></div>
    <p id="status">Бастауға дайын</p>
    <button class="main" id="start">Бастау</button>
    <button id="pause">Тоқтату</button>
    <button id="reset">Қайта бастау</button>
    <p class="count">Аяқталған сессиялар: <b id="done">0</b></p>
  </div>
<script>
var TOTAL = 25 * 60;
var left = TOTAL;
var timer = null;
var done = 0;
var timeEl = document.getElementById("time");
var barEl = document.getElementById("bar");
var statusEl = document.getElementById("status");

function show() {
  var m = Math.floor(left / 60);
  var s = left % 60;
  timeEl.textContent = String(m).padStart(2, "0") + ":" + String(s).padStart(2, "0");
  barEl.style.width = Math.round((TOTAL - left) / TOTAL * 100) + "%";
}
function stop() { clearInterval(timer); timer = null; }

document.getElementById("start").addEventListener("click", function () {
  if (timer) return;
  if (left === 0) left = TOTAL;
  statusEl.textContent = "Жұмыс істеп жатыр";
  timer = setInterval(function () {
    left--;
    show();
    if (left <= 0) {
      stop();
      done++;
      document.getElementById("done").textContent = done;
      statusEl.textContent = "Уақыт бітті, демалыңыз";
    }
  }, 1000);
});
document.getElementById("pause").addEventListener("click", function () {
  if (!timer) return;
  stop();
  statusEl.textContent = "Тоқтатылды";
});
document.getElementById("reset").addEventListener("click", function () {
  stop();
  left = TOTAL;
  show();
  statusEl.textContent = "Бастауға дайын";
});
</script>
</body>
</html>
"""

@app.route("/")
def index():
    return PAGE

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
