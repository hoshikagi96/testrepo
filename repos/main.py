
import unmo

def build_prompt(unmo):
    return "{name}:{responder}>".format(name=unmo.name,
                                        responder=unmo.responder_name)

if __name__ == "__main__":
# スクリプトとして実行したときのみTrue 

    print("Unmo System prototype : proto")
    proto = unmo.Unmo("proto") 
    while True:
        text = input("> ")
        if not text:
            break

        response = proto.dialogue(text)
        print("{prompt}{response}".format(prompt=build_prompt(proto),
                                          response=response))                      