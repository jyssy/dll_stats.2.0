# Electronic general statistics using codes

import re

copies = []
originals = []

with open('969_out.csv') as printout:
    printstats = printout.readlines()
    # printstats = pd.read_csv(printout)
    for line in printstats:
        numbers = re.findall(r"\d+", line)

        i = int(numbers[0])
        print(i)
        print(type(i))

        if 'Copy' in line:
            copies.append(i)
        if 'Original' in line:
            originals.append(i)

    print(sum(copies))
    print(sum(originals))

    with open('elec_out.csv', 'w') as f:  # Could take the step to store this data as memory object instead of file. Consider using the pickle module, or creating a serialization of json or a DB
        f.write('Copy Cataloging = {} /'.format(sum(copies)))
        f.write(' Original Cataloging = {} '.format(sum(originals)))

        # STUFF FOR LATER: print(json.encode({‘copies’: sum(copies), ‘originals’:sum(originals)})) (think about pickling, creating a dB, and maybe use JSON
        # copies += i
    print('General Electronic Stats complete! and yay!')
