from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    # sign up selectors
    btn_sign_up = (By.XPATH, '//*[contains(text(),\'Regístrate\')]')
    use_email = (By.XPATH, '//*[contains(text(),\'Usar correo\')]')
    tbx_nombre = (By.NAME, 'name')
    tbx_email = (By.NAME, 'email')
    dd_mes = (By.XPATH, '//select[@aria-label=\'Mes\']')
    dd_dia = (By.XPATH, '//select[@aria-label=\'Día\']')
    dd_year = (By.XPATH, '//select[@aria-label=\'Año\']')
    btn_next = (By.XPATH, '//*[contains(text(),\'Siguiente\')]')
    btn_registro = (By.XPATH, '//*[contains(text(),\'Registrarse\')]')

    # Login selector
    btn_iniciar_sesion = (By.XPATH, '//*[contains(text(),\'Iniciar sesión\')]')
    tbx_email_tel = (By.NAME, 'session[username_or_email]')
    tbx_login_pass = (By.NAME, 'session[password]')
    btn_iniciar_sesion2 = (By.XPATH, '//*[contains(text(),\'Iniciar sesión\')]')


    # This is de constructor of the class

    def __init__(self, driver):

        super().__init__(driver)

    # This is the create user method
    def create_user(self):
        self.click(self.btn_sign_up)
        self.send_keys(self.tbx_nombre, "Jose Miguel")
        self.click(self.use_email)
        self.send_keys(self.tbx_email, "ajosef478@algo.com")
        self.fill_selector(self.dd_mes, "noviembre")
        self.fill_selector(self.dd_dia, "16")
        self.fill_selector(self.dd_year, "1984")
        #self.click(self.btn_next)
        #self.click(self.btn_next)
        #self.click(self.btn_registro)

    # Login method
    def login(self):
        self.click(self.btn_iniciar_sesion)
        self.send_keys(self.tbx_email_tel, "")
        self.send_keys_enter(self.tbx_login_pass, "")
