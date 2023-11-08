$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$session.Cookies.Add((New-Object System.Net.Cookie("__stripe_mid", "d0e3dd35-db0a-46b1-9c7e-e4b83c3ad531f39cf7", "/", "my.sportpolimi.it")))
$session.Cookies.Add((New-Object System.Net.Cookie("cookieconsent_dismissed", "yes", "/", "my.sportpolimi.it")))
$session.Cookies.Add((New-Object System.Net.Cookie("advanced-frontend", "77ou2ai1i7g1pootrccb7m9ko1", "/", "my.sportpolimi.it")))
$session.Cookies.Add((New-Object System.Net.Cookie("_csrf-frontend", "11658b1232d028c6fea9b6ddfe5907364f367c04a5d9bc973a43335d3ac2c631a:2:{i:0;s:14:`"_csrf-frontend`";i:1;s:32:`"2xcfAsB8byFC-gQghBghaUSM6By_kk3C`";}", "/", "my.sportpolimi.it")))
$session.Cookies.Add((New-Object System.Net.Cookie("SimpleSAML", "4c568ab5c2df5056df20fb6214eb8ca0", "/", "my.sportpolimi.it")))
$session.Cookies.Add((New-Object System.Net.Cookie("SimpleSAMLAuthToken", "_8b555e7d961c7b281fa46ddde4ccbb796b342ed740", "/", "my.sportpolimi.it")))
Invoke-WebRequest -UseBasicParsing -Uri "https://my.sportpolimi.it/booking/get-events?filters=%7B%22city%22%3A%22Milano%22%2C%22playgroundType%22%3A%22%22%2C%22sport%22%3A%22%22%7D&external=2&playground_id=&start=2023-11-09T00%3A00%3A00%2B01%3A00&end=2023-11-10T00%3A00%3A00%2B01%3A00" `
-WebSession $session `
-UserAgent "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0" `
-Headers @{
"Accept" = "*/*"
  "Accept-Language" = "en-GB,en;q=0.5"
  "Accept-Encoding" = "gzip, deflate, br"
  "Referer" = "https://my.sportpolimi.it/booking/calendar?type=athletic_activity&city=Milano"
  "Sec-Fetch-Dest" = "empty"
  "Sec-Fetch-Mode" = "cors"
  "Sec-Fetch-Site" = "same-origin"
  "TE" = "trailers"
}