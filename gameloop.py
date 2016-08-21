# coding: utf-8

def statehandler():
    yield 'ready'
    rooms = {'hall':   {'room': 'Hall',   'transitions': ['office', 'garage'], 'money': 0},
             'office': {'room': 'Office', 'transitions': ['hall', 'globe'],    'money': 0},
             'garage': {'room': 'Garage', 'transitions': ['hall', 'mechanic'], 'money': 0}}
    current_room = rooms['hall']
    yield current_room
    while True:
        print('s: awaiting answer')
        response = yield
        print('s: received {} as answer'.format(response))
        if response:
            if response in current_room['transitions']:
                response_state = rooms.get(response, None)
                if response_state:
                    current_room = response_state
                else:
                    print('s: state unknown (hint: developers fault!)')
                    pass
            else:
                print('s: choice not in transitions')
                pass
        else:
            print('s: response was none-like value')
            pass
        print('s: sending next state')
        yield current_room
        print('s: next state sent')


def view():
    yield 'ready'
    while True:
        print('v: waiting')
        g_in = yield
        print(g_in)
        print('v: need input')
        v_out = input()
        print('v: Sending input')
        yield v_out
        print('v: input sent')

def is_ready(one):
    if one == 'ready':
        print('is ready')
    else:
        raise Exception('First state must be "ready" but is {}'.format(one))

def controller():
    
    s = statehandler()
    s_one = next(s)
    is_ready(s_one)
    v = view()
    v_one = next(v)
    is_ready(v_one)
    # make view wait
    next(v)
    next_state = next(s)
    print('c: make handler wait')
    next(s)
    while True:
        print('c: send state to view')
        vm = v.send(next_state)
        print('c: view answer was {}'.format(vm))
        next(v)
        print('c: send answer to state handler')
        next_state = s.send(vm)
        print('c: next state is {}'.format(next_state))
        next(s)

if __name__ == '__main__':
    controller()
