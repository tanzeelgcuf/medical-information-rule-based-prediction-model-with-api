import webbrowser as wb
def write(diagnosis,disposition,count,keywords):
    f1=open("designs/start.txt","r")
    start=f1.read()
    f1.close()

    f2=open("designs/final.txt","r")
    final=f2.read()
    f2.close()

    make=open("design.html","w")

    table="""<table>
    <tr><th>identities</th><th>values</th></tr>
    <tr><td>Diagnosis</td><td>"""+diagnosis+"""</td></tr>
    <tr><td>Disposition</td><td>"""+disposition+"""</td></tr>
    <tr><td>Total keywords</td><td>"""+count+"""</td></tr>
    <tr><td>Keywords</td><td>"""+keywords+"""</td></tr>
    </table>"""
    make.write(start+table+final)
    make.close()
    wb.open("design.html")


