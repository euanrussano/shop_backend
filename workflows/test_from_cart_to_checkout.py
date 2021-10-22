from utils import Workflow

w= Workflow(verbose=True)
w.set_actions([w.get_cart])
w.run()