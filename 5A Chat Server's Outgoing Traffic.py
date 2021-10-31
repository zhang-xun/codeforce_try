
def main():
    command_set = set()
    results = 0
    while 1:
        try:
            input_command = input()
        except:
            break
        if "+" in input_command:
            command_set.add(input_command[1:])
        elif "-" in input_command:
            command_set.discard(input_command[1:])
        elif ":" in input_command:
            _, message = input_command.split(":")
            results += len(message)*len(command_set)
    
    print(results)
    #return results


if __name__ =="__main__":
    main()