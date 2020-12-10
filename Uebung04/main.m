t = 0:0.1:20;
ta = 1;
tb = 7;
p = 1;

plot(t,eventBound(t, ta, tb, p))
xlabel("t");
ylabel("eventBound(t, t_a, t_b, p)");
title(['Event Bound Function with t_a=', num2str(ta), ' t_b=', num2str(tb),' p=', num2str(p)]);
saveas(gcf,'eventBound','epsc')
