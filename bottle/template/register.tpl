<html>
<head>
    <meta charset="utf-8">
    <title>Hctf</title>
    <link rel="stylesheet" href="../css/spectre.min.css">
    <style>body{padding:10px;}</style>
</head>
<body>
<div class="column col-6 col-sm-12">
  <ul class="tab">
    <li class="tab-item"><a href="/">Home</a></li>
    <li class="tab-item active"><a href="/register">Register</a></li>
    <li class="tab-item"><a href="/login">Login</a></li>
  </ul>
</div>
<div class="column col-3 col-xs-12">
  <form method = 'post' action = '/register'>
  <div class="form-group">
    <label class="form-label" for="input-example-1">Username</label>
    <input class="form-input" id="input-example-1" type="text" name="username" placeholder="">
  </div>
  <div class="form-group">
    <label class="form-label" for="input-example-2">Password</label>
    <input class="form-input" id="input-example-2" type="password" name="password" placeholder="">
  </div>
  <div class="form-group">
    <label class="form-label" for="input-example-3">Confirm</label>
    <input class="form-input" id="input-example-3" type="password" name="confirm" placeholder="">
  </div>
  <h5>{{error}}</h5>
  <button class="btn">register</button>
  </form>
</div>
</body>
</html>