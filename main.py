import pandas as pd
from data.platosRestaurante import platosPopulares
from helpers.crearTabla import crearTabla
tablaMenu=pd.DataFrame(platosPopulares)
print(tablaMenu)