import justpy as jp

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text='Analisys of Course Reviews', classes='text-h3 text-center q-pa-md text-red', v_ripple={'center': True, 'color': 'orange-5'})
    p1 = jp.QDiv(a=wp, text='These graphs represent course review analisys')
    return wp

jp.justpy(app)
