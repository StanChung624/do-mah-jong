from Player import Player

class MANPlayer(Player):

    def draw_card(self, *args, **kwargs):
        kwargs.setdefault("announce")
        return super().draw_card(*args, **kwargs)

    def __action_interface(self)->bool:
        msg = ""
        actions = []
        opt = 1
        if(self.can_eat):
            msg += str(opt) + " eat\n"
            actions.append(self.eat)
            opt+=1
        if(self.can_pon):
            msg += str(opt) + " pon\n"
            actions.append(self.pon)
            opt+=1
        if(self.can_gan):
            msg += str(opt) + " gan\n"
            actions.append(self.gan)
            opt+=1
        if(self.can_win):
            msg += str(opt) + " win\n"
            self.holding.append(self.saw_card)            
            actions.append(self.show)
            opt+=1

        if self.can_eat or self.can_gan or self.can_pon or self.can_win:            
            self.show()
            print("actions:")
            print(msg, "0 none")
            opt = int(input())-1
            if opt >= 0:
                actions[opt]()
                return actions[opt].__name__
            else:
                return None                
            
        else:
            return None

    def action(self, **kwargs)->bool:
        return self.__action_interface()
    
    def ditch(self) -> str:
        return self.__discard_card_interface()

    @Player._sort
    def __discard_card_interface(self):
        id = 1
        for card in self.holding:
            card = ":[" + card + "],"
            print(id, card, end="")
            id += 1
        print()
        return self.discard_card(index=int(input()))