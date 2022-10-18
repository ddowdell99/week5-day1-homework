from app import app
from flask import render_template

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/fav_artists')
def favoiteArtists():
    artists = [{
        'name': 'Montell Fish',
        'picture': 'https://e.snmc.io/i/1200/s/fada62d997a3241a9b1e40ef0e4b8a43/10117371'},
    {
        'name': 'Bryson Tiller',
        'picture': 'https://i.scdn.co/image/ab6761610000e5eb078fdd734b7f0aa782328428'
    },
    {
        'name': 'A$AP Rocky',
        'picture': 'https://www.biography.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTU0MDQyNzUyMzgyODA1NzU1/aap-rocky-from-the-film-monster-poses-for-a-portrait-in-the-youtube-x-getty-images-portrait-studio-at-2018-sundance-film-festival-on-january-22-2018-in-park-city-utah-photo-by-robby-klein_getty-images.jpg'
    },
    {
        'name': 'Kendrick Lamar',
        'picture': 'https://yt3.ggpht.com/V4FqOieQ9y9dnErXPUZNWl1hyLafxIK7F55n5M8LVhPBmEou8kAbNuMlUZx23DoJHvH1sWG56No=s900-c-k-c0x00ffffff-no-rj'
    },
    {
        'name': 'Giveon',
        'picture': 'https://assets.vogue.com/photos/615e0ee86c8d9e425d98d4a0/1:1/w_1065,h_1065,c_limit/Giveon-2021-Zazzo_R8A6100.jpg'
    }]
    return render_template('favorite_artists.html', artists=artists)

