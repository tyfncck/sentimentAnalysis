import sys
import tweepy
from textblob import TextBlob
from PyQt5 import QtWidgets, QtGui, QtCore

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()  # QWidget miras alıyoruz
        self.gui()

    #pencere işlemleri yapmak için fonksiyon
    def gui(self):
        self.Aciklama = QtWidgets.QLabel(self)  #pencerenin icinde label olusturma
        self.Aciklama.setText("TWITTER SENTIMENT ANALYSIS") #etikete yazilacak metin
        self.Aciklama.move(25, 25)  #etiketi tasima komutu

        self.kullaniciAdiLabel = QtWidgets.QLabel(self)
        self.kullaniciAdiLabel.setText("Kullanici Adi")
        self.kullaniciAdiLabel.move(52, 80)

        self.kullaniciAdi = QtWidgets.QTextEdit(self)
        self.kullaniciAdi.setText("tyfncck")
        self.kullaniciAdi.setFixedSize(150, 25)
        self.kullaniciAdi.move(50, 100)

        self.tweetSayisiLabel = QtWidgets.QLabel(self)
        self.tweetSayisiLabel.setText("Tweet Sayisi")
        self.tweetSayisiLabel.move(52, 130)

        self.tweetSayisi = QtWidgets.QTextEdit(self)
        self.tweetSayisi.setText("Max:200")
        self.tweetSayisi.setFixedSize(150, 25)
        self.tweetSayisi.move(50, 150)

        self.yüzdelikLabel = QtWidgets.QLabel(self)
        self.yüzdelikLabel.setText("Yüzdelik Hesabi")
        self.yüzdelikLabel.move(52, 180)

        self.yüzdelik = QtWidgets.QTextEdit(self)
        self.yüzdelik.setFixedSize(150, 100)
        self.yüzdelik.move(50, 195)

        self.hashtagLabel = QtWidgets.QLabel(self)
        self.hashtagLabel.setText("Hashtag")
        self.hashtagLabel.move(52, 350)

        self.hashtag1 = QtWidgets.QTextEdit(self)
        self.hashtag1.setFixedSize(150, 25)
        self.hashtag1.move(50, 370)

        self.yüzdelik2Label = QtWidgets.QLabel(self)
        self.yüzdelik2Label.setText("Yüzdelik Hesabi")
        self.yüzdelik2Label.move(52, 405)

        self.yüzdelik2 = QtWidgets.QTextEdit(self)
        self.yüzdelik2.setFixedSize(150, 100)
        self.yüzdelik2.move(50, 425)

        self.liste = QtWidgets.QTextEdit(self)
        self.liste.setText("Istenilen kullanicinin tweetleri analiz edildiginde bu listede gözükecektir.")
        self.liste.setFixedSize(630, 225)
        self.liste.move(220, 70)

        self.liste2 = QtWidgets.QTextEdit(self)
        self.liste2.setText("Istenilen hashtag' e sahip tweetler analiz edildiginde bu listede gözükecektir.")
        self.liste2.setFixedSize(630, 225)
        self.liste2.move(220, 300)

        self.buton = QtWidgets.QPushButton(self)
        self.buton.setText("Analiz Et")
        self.buton.move(810, 560)

        self.buton2 = QtWidgets.QPushButton(self)
        self.buton2.setText("temizle")
        self.buton2.move(730, 560)

        self.buton3 = QtWidgets.QPushButton(self)
        self.buton3.setText("Hashtag'i Analiz Et")
        self.buton3.move(630, 560)

        self.buton.clicked.connect(self.analiz_et)
        self.buton2.clicked.connect(self.temizle)
        self.buton3.clicked.connect(self.analiz_et2)
        self.show()


    def temizle(self):
        self.liste.clear()
        self.liste2.clear()
        self.yüzdelik.clear()
        self.yüzdelik2.clear()
    def analiz_et(self):
        #bu kisimda API kod degiskenleri tanimlandi
        consumerKey = 'QIUYeq45Efh6o74T3c1OqL8Up'
        consumerKeySecret = 'zd6zhnZ2BjqhSzjgcRmR1aTBqUtsKWy4tjPESqrvXidEheHaCq'
        accessToken = '1895222522-iL40aNNWg9rkkstFEpiz2zthcpzL1WhC7OAMbui'
        accessTokenSecret = 'RcqFmIziBGIE7LFzrGVdO5QZquva0ndlL7PhThgTf12Md'
        #kimlik dogrulamasi yapildi ve API olusturuldu
        auth = tweepy.OAuthHandler(consumerKey, consumerKeySecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)
        kullaniciAdi = self.kullaniciAdi.toPlainText()
        tweewSayisi = self.tweetSayisi.toPlainText()
        #kullanicinin istenilen adette tweete cekildi ve degiskene atildi
        publicTweets = api.user_timeline(screen_name=kullaniciAdi, count=tweewSayisi)
        pozitifTweetler = []
        negatifTweetler = []
        nötrTweetler = []
        for tweet in publicTweets:
            print(tweet.text)
            analiz = TextBlob(tweet.text)
            print(analiz.sentiment)
            if analiz.sentiment[0] > 0:
                pozitifTweetler.append(tweet.text)
                self.liste.append("pozitif tweet:\n" + tweet.text)
            elif analiz.sentiment[0] < 0:
                negatifTweetler.append(tweet.text)
                self.liste.append("\n\nnegatif tweet:\n" + tweet.text)
            else:
                nötrTweetler.append(tweet.text)
                self.liste.append("\n\nnötr tweet:\n" + tweet.text)

        pozitifTweetOrani = 100 * (len(pozitifTweetler)/len(publicTweets))
        negatifTweetOrani = 100 * (len(negatifTweetler)/len(publicTweets))
        nötrTweetOrani = 100 * (len(nötrTweetler)/len(publicTweets))

        self.yüzdelik.append("pozitif tweet Orani: \n%" + format(pozitifTweetOrani))
        self.yüzdelik.append("negatif tweet Orani: \n%" + format(negatifTweetOrani))
        self.yüzdelik.append("nötr tweet Orani: \n%" + format(nötrTweetOrani))

    def analiz_et2(self):
        consumerKey = 'QIUYeq45Efh6o74T3c1OqL8Up'
        consumerKeySecret = 'zd6zhnZ2BjqhSzjgcRmR1aTBqUtsKWy4tjPESqrvXidEheHaCq'
        accessToken = '1895222522-iL40aNNWg9rkkstFEpiz2zthcpzL1WhC7OAMbui'
        accessTokenSecret = 'RcqFmIziBGIE7LFzrGVdO5QZquva0ndlL7PhThgTf12Md'
        # kimlik dogrulamasi yapildi ve API olusturuldu
        auth = tweepy.OAuthHandler(consumerKey, consumerKeySecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)
        hashtag = self.hashtag1.toPlainText()
        tweets = api.search("'" + hashtag + "'")
        pozitifTweetlerHashtag = []
        negatifTweetlerHashtag = []
        nötrTweetlerHashtag = []
        for tweet in tweets:
            analiz2 = TextBlob(tweet.text)
            if analiz2.sentiment[0] > 0:
                pozitifTweetlerHashtag.append(tweet.text)
                self.liste2.append("pozitif tweet:\n" + tweet.text)
            elif analiz2.sentiment[0] < 0:
                negatifTweetlerHashtag.append(tweet.text)
                self.liste2.append("\n\nnegatif tweet:\n" + tweet.text)
            else:
                nötrTweetlerHashtag.append(tweet.text)
                self.liste2.append("\n\nnötr tweet:\n" + tweet.text)

        pozitifTweetHashtagOrani = 100 * (len(pozitifTweetlerHashtag) / len(tweets))
        negatifTweetHashtagOrani = 100 * (len(negatifTweetlerHashtag) / len(tweets))
        nötrTweetHashtagOrani = 100 * (len(nötrTweetlerHashtag) / len(tweets))

        self.yüzdelik2.append("pozitif tweet Orani: \n%" + format(pozitifTweetHashtagOrani))
        self.yüzdelik2.append("negatif tweet Orani: \n%" + format(negatifTweetHashtagOrani))
        self.yüzdelik2.append("nötr tweet Orani: \n%" + format(nötrTweetHashtagOrani))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # pencere uygulaması oluşturuyoruz
    pencere = Pencere()   #pencere nesnesi oluşturuyoruz
    pencere.setWindowTitle("Sentiment Analysis") #pencere basligini girdik
    pencere.setFixedSize(900, 600)
    sys.exit(app.exec_())  #pencereyi açık tutmak için