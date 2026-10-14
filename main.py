from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window

# ضبط خلفية التطبيق بيضاء
Window.clearcolor = (1, 1, 1, 1)

class CentraleApp(App):
    def build(self):
        self.title = "Centrale AMM Complet"
        
        # حاوية رئيسية عمودية مع مسافات (padding)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # 1. العنوان الرئيسي
        lbl_title = Label(
            text="Centrale Khaled AMM\nDosage Complet",
            font_size='22sp',
            bold=True,
            color=(13/255, 92/255, 182/255, 1), # اللون الأزرق #0d5cb6
            halign='center',
            size_hint_y=None,
            height=70
        )
        layout.add_widget(lbl_title)
        
        # 2. نص "Type de béton:"
        layout.add_widget(Label(
            text="Type de béton:", 
            color=(0, 0, 0, 1), # لون أسود واضح
            size_hint_y=None, 
            height=25
        ))
        
        # 3. القائمة المنسدلة (Spinner)
        self.combo = Spinner(
            text="B2 - 340Kg",
            values=("B2 - 340Kg", "B20 - 210Kg", "B25 - 310Kg"),
            size_hint_y=None,
            height=45,
            background_normal='',
            background_color=(0.9, 0.9, 0.9, 1), # لون رمادي فاتح بحال الصورة
            color=(0, 0, 0, 1) # كتابة سوداء
        )
        layout.add_widget(self.combo)
        
        # 4. نص "Quantité en m3:"
        layout.add_widget(Label(
            text="Quantité en m3:", 
            color=(0, 0, 0, 1), 
            size_hint_y=None, 
            height=25
        ))
        
        # 5. حقل إدخال الكمية
        self.entree_qte = TextInput(
            text="1",
            multiline=False,
            input_filter='float',
            halign='center',
            font_size='20sp',
            size_hint_y=None,
            height=45
        )
        layout.add_widget(self.entree_qte)
        
        # 6. زر الحساب الأزرق
        btn_calculer = Button(
            text="CALCULER DOSAGE",
            font_size='16sp',
            bold=True,
            background_normal='', 
            background_color=(13/255, 92/255, 182/255, 1), # الأزرق الملكي
            color=(1, 1, 1, 1), # كتابة بيضاء
            size_hint_y=None,
            height=50
        )
        btn_calculer.bind(on_press=self.calculer)
        layout.add_widget(btn_calculer)
        
        # 7. مساحة عرض النتائج (Label كبير يأخذ المساحة المتبقية)
        self.resultat = Label(
            text="Résultat ici...",
            font_size='16sp',
            bold=True,
            color=(0, 0, 0, 1), # إجبار لون النص يكون أسود باش يبان كامل
            halign='left',
            valign='top',
            size_hint_y=1 # يأخذ باقي الشاشة كاملة لفوق
        )
        # لضمان محاذاة النص لليسار ولفوق بشكل صحيح
        self.resultat.bind(size=self.resultat.setter('text_size'))
        layout.add_widget(self.resultat)
        
        return layout

    def calculer(self, instance):
        try:
            q = float(self.entree_qte.text)
            type_sel = self.combo.text
            
            if "B2" in type_sel and "B20" not in type_sel:
                nom, ciment, sl, g1, g2 = "B2", 340, 754, 565, 566
            elif "B20" in type_sel:
                nom, ciment, sl, g1, g2 = "B20", 210, 807, 405, 767
            elif "B25" in type_sel:
                nom, ciment, sl, g1, g2 = "B25", 310, 770, 526, 609

            t_ciment = ciment * q
            t_sl = sl * q
            t_g1 = g1 * q
            t_g2 = g2 * q
            t_sacs = t_ciment / 50
            
            # تم صياغة النص بوضوح مع أسطر واضحة لتظهر على شاشة الهاتف
            txt = (
                f"=== {nom} pour {q} m3 ===\n\n"
                f"CIMENT : {t_ciment:.0f} Kg ({t_sacs:.1f} sacs)\n"
                f"SABLE (SL) : {t_sl:.0f} Kg\n"
                f"G1 : {t_g1:.0f} Kg\n"
                f"G2 : {t_g2:.0f} Kg\n\n"
                f"Pour 1 m3 : {ciment} / {sl} / {g1} / {g2}"
            )
            
            self.resultat.text = txt
        except Exception as e:
            self.resultat.text = "Erreur de saisie!"

if __name__ == '__main__':
    CentraleApp().run()
