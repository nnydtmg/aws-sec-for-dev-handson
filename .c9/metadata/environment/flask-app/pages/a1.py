{"filter":false,"title":"a1.py","tooltip":"/flask-app/pages/a1.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":19,"column":42},"action":"remove","lines":["from flask import (","    Blueprint,","    request,","    render_template_string",")","","bp = Blueprint(","    \"a1\", __name__,","    template_folder='templates',","    static_folder='static'",")","","@bp.route(\"/A1\")","def a1():","    ### Server-Side Template Injection","    name = request.args.get(\"name\", \"\")","    with open(\"templates/a1.html\") as f:","        template = f.read()","    content = template.replace(\"{{ name }}\", name)","    return render_template_string(content)"],"id":2},{"start":{"row":0,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["from flask import (","    Blueprint,","    request,","    render_template",")","","bp = Blueprint(","    \"a1\", __name__,","    template_folder='templates',","    static_folder='static'",")","","@bp.route(\"/A1\")","def a1():","    name = request.args.get(\"name\", \"\")","    return render_template(\"a1.html\", name=name)",""]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":16,"column":0},"end":{"row":16,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":30,"mode":"ace/mode/python"}},"timestamp":1676182944133,"hash":"3f6320565402899629a315a14628e5fd18bcb029"}