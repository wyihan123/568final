from flask import Flask, render_template, request
import config
import aicontent

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())



@app.route('/product-description', methods=["GET", "POST"])
def productDescription():

    if request.method == 'POST':
        submission = request.form['productDescription']
        query = "Generate a detailed product descriptions for: {}".format(submission)
        openAIAnswer = aicontent.OpenAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('product-description.html', **locals())



@app.route('/cold-emails', methods=["GET", "POST"])
def coldEmails():

    if request.method == 'POST':
        submission = request.form['coldEmails']
        query = "Generate a cold email to potential clients about: {}".format(submission)
        openAIAnswerUnformatted = aicontent.OpenAIQuery(query)
        openAIAnswer = openAIAnswerUnformatted.replace('\n', '<br>')
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('cold-emails.html', **locals())



@app.route('/social-media', methods=["GET", "POST"])
def socialMedia():

    if request.method == 'POST':
        submission = request.form['socialMedia']

        part1 = aicontent.OpenAIQuery("Generate a social media tweet about: {}. \n".format(submission))
        part2 = aicontent.OpenAIQuery("Generate a hashtags about: {}".format(submission))

        openAIAnswer = """
        {} {}
        {}
        """.format(submission, part1, part2)

        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('social-media.html', **locals())



@app.route('/video-description', methods=["GET", "POST"])
def videoDescription():

    if request.method == 'POST':
        submission = request.form['videoDescription']
        query = "Generate a detailed video descriptions for video that related to: {}".format(submission)
        openAIAnswer = aicontent.OpenAIQuery(query)
        prompt = 'AI Suggestions for {} are:'.format(submission)

    return render_template('video-description.html', **locals())




if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
