import instaloader

def main():
    # Instaloader nesnesi oluştur
    loader = instaloader.Instaloader()

    with open('kullanicilar.txt','r') as file:
      for username in file.readlines():
            profile_name = username.strip()
            print(f"Fotografları konumlandiran profil: {profile_name}")
            try:
                user_profile = instaloader.Profile.from_username(loader.context, profile_name)
            except Exception as e:
                print(f"Profil bulunamadi ya da başka hata! : {profile_name}\nHata mesaji: {e}")
                continue

            loader.download_profile(user_profile, profile_pic=True, fast_update=True)

if __name__ == "__main__":
    main()
