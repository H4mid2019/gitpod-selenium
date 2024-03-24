

def test_google_search(py):
    py.visit("https://google.com")
    py.getx('//button[@id][@data-ved]/div[contains(text(),"Alles accepteren")]').click()
    py.screenshot("gg.png")
    py.get("[name='q']").type("Pylenium")
    py.get("[name='btnK']").submit()
    assert py.should().contain_title("Pylenium")