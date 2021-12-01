class registroDeZonas:

    @staticmethod
    def listadoZonas(eventos):
        zonas = ''
        i = 0
        for zona in eventos['Nombre']:
            zonas += f'{i} |' + zona + '\n'
            i += 1
        return zonas
