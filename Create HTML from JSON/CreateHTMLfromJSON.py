#############################################
# 
#   To convert JSON to an HTML file, you can use the following Python code. 
#   This code reads a JSON file (in this case, "Swagger.json"), and generates an HTML file ("api-docs.html") 
# that uses the Redoc library to display the API documentation in a user-friendly format.
#
# Make sure you have the "Swagger.json" file in the same directory as this script, and then run the script to create the "api-docs.html" file.
#############################################





import json

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>API Docs</title>
</head>
<body>
  <div id="redoc-container"></div>
  <script src="https://cdn.jsdelivr.net/npm/redoc/bundles/redoc.standalone.js"></script>
  <script>
    var spec = %s;
    Redoc.init(spec, {}, document.getElementById("redoc-container"));
  </script>
</body>
</html>
"""

with open("Swagger.json") as f:
    spec = json.load(f)

with open("api-docs.html", "w") as out:
    out.write(HTML_TEMPLATE % json.dumps(spec))