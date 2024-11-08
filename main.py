import pyxel

class TamagotchiApp:
    def __init__(self):
        pyxel.init(160, 120, title="Tamagotchi App")
        self.character_x = 70
        self.character_y = 50
        self.fullness = 50  # 満腹度
        self.fun = 50       # 楽しさ
        self.health = 100   # 健康度
        pyxel.run(self.update, self.draw)
    
    def update(self):
        # 時間経過でステータスを減少
        if pyxel.frame_count % 60 == 0:
            self.fullness = max(0, self.fullness - 1)
            self.fun = max(0, self.fun - 1)
            self.health = max(0, self.health - 0.5)
        
        # エサをあげるアクション（スペースキー）
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.feed()

        # 遊ぶアクション（Aキー）
        if pyxel.btnp(pyxel.KEY_A):
            self.play()

    def feed(self):
        # 満腹度を増加（上限100）
        self.fullness = min(100, self.fullness + 10)
    
    def play(self):
        # 楽しさを増加（上限100）
        self.fun = min(100, self.fun + 10)
    
    def draw(self):
        pyxel.cls(0)
        # キャラクター表示
        pyxel.circ(self.character_x, self.character_y, 10, 9)
        
        # ステータスバーの描画
        pyxel.rect(10, 10, self.fullness, 5, 8)
        pyxel.text(10, 17, f"Fullness: {self.fullness}", 7)
        
        pyxel.rect(10, 30, self.fun, 5, 11)
        pyxel.text(10, 37, f"Fun: {self.fun}", 7)
        
        pyxel.rect(10, 50, int(self.health), 5, 10)
        pyxel.text(10, 57, f"Health: {int(self.health)}", 7)

TamagotchiApp()
