from flask import Flask, jsonify, request
from yt_dlp import YoutubeDL

app = Flask(__name__)

def get_direct_url(video_url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'forceurl': True,
        'forcejson': True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            formats = info_dict.get('formats', [])

            # نختار أفضل جودة MP4 قابلة للتشغيل مباشر
            for f in reversed(formats):
                if f.get('ext') == 'mp4' and f.get('url'):
                    return {"success": "1", "url": f.get('url')}

            return {"success": "0", "error": "No suitable format found"}

    except Exception as e:
        return {"success": "0", "error": str(e)}

# YouTube
@app.route('/youtube/')
def youtube():
    url = request.args.get('url')
    return jsonify(get_direct_url(url))

# TikTok
@app.route('/tiktok/')
def tiktok():
    url = request.args.get('url')
    return jsonify(get_direct_url(url))

# Facebook
@app.route('/facebook/')
def facebook():
    url = request.args.get('url')
    return jsonify(get_direct_url(url))

# Instagram Reels
@app.route('/instagram/reel/')
def instagram_reel():
    url = request.args.get('url')
    return jsonify(get_direct_url(url))

# Instagram Image (هنا لو الصورة فيديو بيمشي، أما صور سابتة فقد تحتاج تعديل)
@app.route('/instagram/image/')
def instagram_image():
    url = request.args.get('url')
    return jsonify(get_direct_url(url))

# Snapchat
@app.route('/snapchat/')
def snapchat():
    url = request.args.get('url')
    return jsonify(get_direct_url(url))

if __name__ == '__main__':
    app.run(debug=True)
