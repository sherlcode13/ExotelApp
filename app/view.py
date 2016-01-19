from app import app
from flask import  render_template,request,flash
import base64, requests

def do(number):
    sid='springboardinvestments1'
    usrPass= sid + ':a4c340d7bbcf4c7a650435948c569cf88aa18c19'
    authorisation_header_value = 'Basic ' + base64.b64encode(usrPass)
    exotelUrl= 'http://twilix.exotel.in/v1/Accounts/' + sid + '/CustomerWhitelist/'
    payload={'VirtualNumber':' 7838220013','Number[]':number}
    result=requests.post(exotelUrl,headers={"Authorization": authorisation_header_value},data=payload)
    if result.status_code == requests.codes.ok :
        app.logger.warning(payload['Number[]']+'is added in whitelist')
    else:
        app.logger.warning(payload['Number[]']+' is not authorised by Exotel')
    app.logger.info('Info')
    return result


@app.route('/',methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        number=request.form['number']
        if do(number).status_code == requests.codes.ok :
            message = "Successfully whitlisted " + number
        else:
            message = number + " is not authorised."
        return render_template('index.html', message=message)
    else:
        return render_template('index.html')
        
