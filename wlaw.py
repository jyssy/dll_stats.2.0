# Getting WLAW data out of the monthly reporting

import re

wlaw = []

with open('stats_out.csv') as printout:
    printstats = printout.readlines()
    # printstats = pd.read_csv(printout)
    for line in printstats:
        numbers = re.findall(r"\d+", line)

        i = int(numbers[0])
        print(i)
        print(type(i))

        if 'WLAW' in line:
            wlaw.append(i)

    print(sum(wlaw))

    with open('wlaw_out.csv', 'w') as f:  # Could take the step to store this data as memory object instead of file. Consider using the pickle module, or creating a serialization of json or a DB
        f.write('WLAW Copies added = {} '.format(sum(wlaw)))

        # STUFF FOR LATER: print(json.encode({‘copies’: sum(copies), ‘originals’:sum(originals)})) (think about pickling, creating a dB, and maybe use JSON
        # copies += i

    print('WLAW run! and yay!')
