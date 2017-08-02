import numpy as np

from growth_procs import unit_sample_on_sphere,\
     direction_to,\
     normalize_length,\
     get_entity,\
     prepare_next_front

L_NORM=1.0

def extend_front(front,seed,constellation,interstitial) :
    # attract by a different neuron, get information
    other_entities = get_entity("substance_x",constellation)

    # fetch the case that no such entities exists    
    if len(other_entities) == 0 :
        new_pos =front.xyz + np.array([L_NORM,0,0])
    else :
        rnd_dir = unit_sample_on_sphere()
        dir_to_entity = direction_to(front,other_entities,what="nearest")
        dir_to_entity = normalize_length(dir_to_entity,1.0) + rnd_dir*0.
        new_pos = front.xyz + normalize_length(dir_to_entity,L_NORM)
    new_front = prepare_next_front(front,new_pos,set_radius=0.5)

    return [new_front]
