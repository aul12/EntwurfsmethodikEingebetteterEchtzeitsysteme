function E = eventBound(t,ta,tb,p)
    n_minus = ceil(ta/p);
    n_plus_tmp = ceil(tb/p)-1;
    n_plus = floor(t./p);
    n_plus(n_plus > n_plus_tmp) = n_plus_tmp;
   
    E=n_plus - n_minus + 1;
    E(n_minus > n_plus) = 0;
end
