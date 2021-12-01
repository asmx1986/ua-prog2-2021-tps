import json, time, os
import Import_index

class Json:
    def __init__(self) -> None:
        pass

    def save_json(self, sensors_formatted):
        with open('./src/sensors_persisted.json', 'w', encoding='utf-8') as f:
            json.dump(sensors_formatted, f, ensure_ascii=False, indent=4)
    
    def load_json_from_file(self) -> dict:
        try:
            items = list(range(0, 35))
            l = len(items)

            # Initial call to print 0% progress
            printProgressBar(0, l, prefix = 'Progreso de carga:', suffix = 'Complete', length = 50)
            for i, item in enumerate(items):
                Import_index.erase_screen()

                # Update Progress Bar
                print("---- Cargando datos ----")
                printProgressBar(i + 1, l, prefix = 'Progreso de carga:', suffix = 'Complete', length = 50)
                time.sleep(0.02)

                
            print("---- Datos cargados con éxito ----")
            time.sleep(1)
            Import_index.erase_screen()

            with open('./src/sensors_persisted.json') as json_file:
                data = json.load(json_file)

                return data
        except:
            return dict()



# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()