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
    <li class="tab-item active"><a href="/user">User</a></li>
    <li class="tab-item"><a href="/logout">Logout</a></li>
  </ul>
</div>
<div class="column col-12">
  <div class="empty">
  <p class="empty-title h5">Hello {{username}}</p>
  <p class="empty-title h8">now you can submit url</p>
    <form method='post'>
    <div class="empty-action input-group input-inline">
      <input class="form-input" type="text" name="url" placeholder="">
    </div>
    </br>
    <p class="empty-title h8">{{captcha}}</p>
    <div class="empty-action input-group input-inline">
      <input class="form-input" type="text" name="captcha" placeholder="">
      <button class="btn btn-primary input-group-btn">Submit</button>
    </div>
    </form>
  <p class="empty-title h8">{{errors}}</p>
  </div>
</div>
<body>
</html>