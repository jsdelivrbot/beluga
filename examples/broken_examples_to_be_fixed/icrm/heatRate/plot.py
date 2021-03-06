from beluga.visualization import BelugaPlot

# plots = BelugaPlot('./data_2500_ep4.dill',default_sol=-1,default_step=-1, renderer='matplotlib')
# plots = BelugaPlot('./data-flydown.dill',default_sol=-1,default_step=-1, renderer='matplotlib')
plots = BelugaPlot('./data-1k2-eps6-eps7.dill',default_sol=-1,default_step=-1, renderer='matplotlib')
# plots = BelugaPlot('./data_1200_5k_1deg_ep6.dill',default_sol=-1,default_step=-1, renderer='matplotlib')

plots.add_plot().line('theta*180/3.14','h/1000')                    \
                .xlabel('Downrange (deg)').ylabel('h (km)')      \
                .title('Altitude vs. Downrange')

plots.add_plot().line('t','k*sqrt(rho0*exp(-h/H)/rn)*v**3/1e4')                    \
                .line('t','qdotMax/1e4')    \
                .xlabel('t (s)').ylabel('Heat Rate (W/cm^2)')      \
                .title('Heat Rate vs. Time')

# plots.add_plot().line('t','sqrt(D^2+L^2)/(mass*9.81)') \
#                 .xlabel('t (s)').ylabel('G-Loading')      \
#                 .title('G-Loading vs. Time')
plots.add_plot().line('t','v/1e3') \
                .xlabel('t (s)').ylabel('Heat rate')      \
                .title('Heatrate vs. Time')

plots.add_plot().line('t','gam*180/pi') \
                .xlabel('t (s)').ylabel('FPA (deg)')      \
                .title('FPA')
plots.render()
