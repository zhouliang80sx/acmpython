import java.awt.*;   
import java.awt.event.*;   
import javax.swing.*;    
   
public class voronoi extends JFrame implements ActionListener, ItemListener   
{   
    Container cp;   
    Graphics g;   
    Node_paint T;   
    CustomPanel mypanel;   
    JButton bt1,bt_reset;   
    JLabel lb;   
    JComboBox cb;   
    JCheckBox tribox;   
       
    private String name[] =    
    {"Brute Force","Divide-and-Conquer"};   
    int N=0;   
    int mx, my;   
    int saveindex,startindex;   
    static double vxt= 0.00, vyt=0.00, vxn=1.00, vyn=0.00;   
    int tmp = 100, count1 = 0,min = 9999;   
    private int nx[] = new int[100];   
    private int ny[] = new int[100]; //Node?y?D   
    private int edge[][] = new int [100][100];   
    int visit[] = new int[100];   
    Color []color = new Color[100];   
    int color1 = 0;   
       
    public voronoi()   
    {   
        super ("Voronoi");   
        setBounds (200,20,500,500);   
           
        cp = getContentPane();   
        cp.setBackground(getBackground());   
        cp.setLayout(new FlowLayout(FlowLayout.CENTER));   
           
        lb = new JLabel("Voronoi Diagram");   
        cp.add(lb);   
        g = getGraphics();   
        T = new Node_paint(getGraphics());   
        mypanel = new CustomPanel();   
        mypanel.setBackground(Color.white);   
        cp.add(mypanel);   
           
        JPanel pn = new JPanel();   
        pn.setLayout( new FlowLayout(FlowLayout.LEFT));   
        cp.add(pn);   
           
   
        bt1 = new JButton("Start");   
        bt_reset = new JButton("Reset");   
        bt1.addActionListener(this);       
        bt_reset.addActionListener(this);      
        pn.add(bt1);   
        pn.add(bt_reset);   
        tribox = new JCheckBox("Delaunay Triangle");   
        tribox.addItemListener(this);   
        cp.add(tribox);   
           
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);   
        setVisible(true);      
    }   
       
    public static void main(String[] args)   
    {   
        voronoi app = new voronoi();   
           
    }   
       
    public void actionPerformed(ActionEvent evt)   
    {   
        if (evt.getSource() == bt1){   
            if (cb.getSelectedIndex() == 0)   
                brute();   
            if (cb.getSelectedIndex() == 1){   
                for (;;){   
                    if (tmp == startindex){                    
                        break;   
                    }   
                    warpping();    
                }   
                   
                divided_and_conquer();     
            }   
        }   
        if (evt.getSource() == bt_reset){   
            mypanel.repaint();   
            N=0;   
            vxt= 0.00; vyt=0.00; vxn=1.00; vyn=0.00;   
            min = 9999; count1 = 0; tmp = 100;    
            for (int i=0;i<100;i++){   
                for (int j=0;j<100;j++)   
                    edge[i][j] = 0;    
            }   
            for (int i=0;i<100;i++)   
                visit[i] = 0;   
        }   
    }   
    public void itemStateChanged(ItemEvent e)   
    {   
        if (e.getSource() == tribox){   
            if (e.getStateChange() == ItemEvent.SELECTED){   
                color1 = 1;   
                divided_and_conquer();   
            }   
            if (e.getStateChange() == ItemEvent.DESELECTED){   
                color1 = 0;    
                divided_and_conquer();   
            }   
        }      
    }   
       
    public void brute()   
    {   
        double d;   
        double Min = 999.0;   
        int index=0;   
        int R, G, B;   
           
        for (int j=0;j<N;j++){   
            R = (int)(Math.random()*255);   
            G = (int)(Math.random()*255);   
            B = (int)(Math.random()*255);   
            color[j] = new Color(R,G,0);   
        }   
        for (int x=1;x<=450;x++){   
            for (int y=1;y<=500;y++){   
                for (int i=0;i<N;i++){   
                    d = Math.sqrt((x-nx[i])*(x-nx[i])+(y-ny[i])*(y-ny[i]));   
                    if (d < Min){   
                        Min = d;   
                        index = i;   
                    }   
                           
                }   
                g.setColor(color[index]);   
                g.drawLine(x,y+(500-2*y),x,y+(500-2*y));   
                Min = 999.0;   
            }      
        }   
        for (int j=0;j<N;j++){   
            T.getnode(j);   
            T.drwnode();       
        }      
    }   
    public void divided_and_conquer()   
    {   
           
        int d1, d2, d3;   
        int a, b;   
        double dis;   
        int count=0;   
        int Vector_x, Vector_y;   
        double ip_check, va, vb;   
           
           
        g.setColor(Color.black);   
           
        if (N == 2){   
            Vector_x = nx[0] - nx[1];   
            Vector_y = (ny[0]+(500-2*ny[0])) - (ny[1]+(500-2*ny[1]));   
               
            g.drawLine((nx[0]+nx[1])/2,(ny[0]+ny[1])/2+(500-(ny[0]+ny[1])),Vector_y*100+(nx[0]+nx[1])/2,-Vector_x*100+(ny[0]+ny[1])/2);   
            g.drawLine((nx[0]+nx[1])/2,(ny[0]+ny[1])/2+(500-(ny[0]+ny[1])),-Vector_y*100+(nx[0]+nx[1])/2,Vector_x*100+(ny[0]+ny[1])/2);   
        }   
           
        for (int i=0;i<N;i++){   
            for (int j=i+1;j<N;j++){   
                for (int k=j+1;k<N;k++){   
                    d1 = nx[i]*nx[i]+ny[i]*ny[i];   
                    d2 = nx[j]*nx[j]+ny[j]*ny[j];   
                    d3 = nx[k]*nx[k]+ny[k]*ny[k];   
                    a = ((d1*ny[j]+d2*ny[k]+d3*ny[i]-d3*ny[j]-d2*ny[i]-d1*ny[k])/(nx[i]*ny[j]+nx[j]*ny[k]+nx[k]*ny[i]-nx[k]*ny[j]-nx[j]*ny[i]-nx[i]*ny[k]))/2;   
                    b = ((nx[i]*d2+nx[j]*d3+nx[k]*d1-nx[k]*d2-nx[j]*d1-nx[i]*d3)/(nx[i]*ny[j]+nx[j]*ny[k]+nx[k]*ny[i]-nx[k]*ny[j]-nx[j]*ny[i]-nx[i]*ny[k]))/2;     
           
                    dis = Math.sqrt((nx[i]-a)*(nx[i]-a)+(ny[i]-b)*(ny[i]-b))*2;   
                    for (int l=0;l<N;l++){   
                        if (Math.sqrt((nx[l]-a)*(nx[l]-a)+(ny[l]-b)*(ny[l]-b))<(dis/2)&&l!=i&&l!=j&&l!=k)   
                            count++;               
                    }   
                    if (count == 0){   
                        if (color1 == 1)   
                            g.setColor(Color.orange);   
                        else   
                            g.setColor(Color.white);   
                        g.drawLine(nx[i],ny[i]+(500-2*ny[i]),nx[j],ny[j]+(500-2*ny[j]));   
                        g.drawLine(nx[j],ny[j]+(500-2*ny[j]),nx[k],ny[k]+(500-2*ny[k]));   
                        g.drawLine(nx[k],ny[k]+(500-2*ny[k]),nx[i],ny[i]+(500-2*ny[i]));   
                        //g.drawOval(a-5,b-5+(350-2*b),10,10);   
                        //g.drawOval(a-((int)dis/2),b-((int)dis/2)+(350-2*b),(int)dis,(int)dis);   
                        g.setColor(Color.black);   
                        if (edge[i][j] != 1)   
                            g.drawLine(a,b+(500-2*b),(nx[i]+nx[j])/2,(ny[i]+ny[j])/2+(500-(ny[i]+ny[j])));   
                        if (edge[j][k] != 1)   
                            g.drawLine(a,b+(500-2*b),(nx[j]+nx[k])/2,(ny[j]+ny[k])/2+(500-(ny[j]+ny[k])));   
                        if (edge[i][k] != 1)   
                            g.drawLine(a,b+(500-2*b),(nx[i]+nx[k])/2,(ny[i]+ny[k])/2+(500-(ny[i]+ny[k])));   
                           
                        if (edge[i][j] == 1){   
                            ev(nx[k],nx[j],ny[k],ny[j]);   
                            va = vxt;   vb = vyt;   
                            ev(nx[k],nx[i],ny[k],ny[i]);   
                            ip_check = nip(va,vxt,vb,vyt);   
                            Vector_x = (nx[i]+nx[j])/2 - a;   
                            Vector_y = ((ny[i]+ny[j])/2+(500-(ny[i]+ny[j]))) - (b+(500-2*b));   
                            if (ip_check < 0){   
                                Vector_x = -Vector_x;   
                                Vector_y = -Vector_y;   
                            }   
                            g.drawLine(a,b+(500-2*b),Vector_x*100+a,Vector_y*100+b);       
                                       
                               
                        }   
                        if (edge[j][k] == 1){   
                            ev(nx[i],nx[j],ny[i],ny[j]);   
                            va = vxt;   vb = vyt;   
                            ev(nx[i],nx[k],ny[i],ny[k]);   
                            ip_check = nip(va,vxt,vb,vyt);   
                            Vector_x = (nx[j]+nx[k])/2 - a;   
                            Vector_y = ((ny[j]+ny[k])/2+(500-(ny[j]+ny[k]))) - (b+(500-2*b));   
                            if (ip_check < 0){   
                                Vector_x = -Vector_x;   
                                Vector_y = -Vector_y;   
                            }   
                            g.drawLine(a,b+(500-2*b),Vector_x*100+a,Vector_y*100+b);   
                        }   
                        if (edge[i][k] == 1){   
                            ev(nx[j],nx[i],ny[j],ny[i]);   
                            va = vxt;   vb = vyt;   
                            ev(nx[j],nx[k],ny[j],ny[k]);   
                            ip_check = nip(va,vxt,vb,vyt);   
                            Vector_x = (nx[i]+nx[k])/2 - a;   
                            Vector_y = ((ny[i]+ny[k])/2+(500-(ny[i]+ny[k]))) - (b+(500-2*b));   
                            if (ip_check < 0){   
                                Vector_x = -Vector_x;   
                                Vector_y = -Vector_y;   
                            }   
                            g.drawLine(a,b+(500-2*b),Vector_x*100+a,Vector_y*100+b);   
                        }   
                           
                    }   
                       
           
                    //g.drawOval(a-((int)dis/2),b-((int)dis/2),(int)dis,(int)dis);   
                count=0;       
                }   
                   
            }   
        }   
           
        for (int i=0;i<N;i++){   
            for (int j=i+1;j<N;j++){   
                for (int k=j+1;k<N;k++){   
                    d1 = nx[i]*nx[i]+ny[i]*ny[i];   
                    d2 = nx[j]*nx[j]+ny[j]*ny[j];   
                    d3 = nx[k]*nx[k]+ny[k]*ny[k];   
                    a = ((d1*ny[j]+d2*ny[k]+d3*ny[i]-d3*ny[j]-d2*ny[i]-d1*ny[k])/(nx[i]*ny[j]+nx[j]*ny[k]+nx[k]*ny[i]-nx[k]*ny[j]-nx[j]*ny[i]-nx[i]*ny[k]))/2;   
                    b = ((nx[i]*d2+nx[j]*d3+nx[k]*d1-nx[k]*d2-nx[j]*d1-nx[i]*d3)/(nx[i]*ny[j]+nx[j]*ny[k]+nx[k]*ny[i]-nx[k]*ny[j]-nx[j]*ny[i]-nx[i]*ny[k]))/2;     
           
                    dis = Math.sqrt((nx[i]-a)*(nx[i]-a)+(ny[i]-b)*(ny[i]-b))*2;   
                    for (int l=0;l<N;l++){   
                        if (Math.sqrt((nx[l]-a)*(nx[l]-a)+(ny[l]-b)*(ny[l]-b))<(dis/2)&&l!=i&&l!=j&&l!=k)   
                            count++;               
                    }   
                    if (count == 0){   
                        //if (edge[i][j] != 1){   
                            ev(nx[k],nx[j],ny[k],ny[j]);   
                            va = vxt;   vb = vyt;   
                            ev(nx[k],nx[i],ny[k],ny[i]);   
                            ip_check = nip(va,vxt,vb,vyt);   
                            if (ip_check < 0){   
                                g.setColor(Color.white);   
                                g.drawLine(a,b+(500-2*b),(nx[i]+nx[j])/2,(ny[i]+ny[j])/2+(500-(ny[i]+ny[j])));   
                            }   
                        //}   
                        //if (edge[j][k] != 1){   
                            ev(nx[i],nx[j],ny[i],ny[j]);   
                            va = vxt;   vb = vyt;   
                            ev(nx[i],nx[k],ny[i],ny[k]);   
                            ip_check = nip(va,vxt,vb,vyt);   
                            if (ip_check < 0){   
                                g.setColor(Color.white);   
                                g.drawLine(a,b+(500-2*b),(nx[j]+nx[k])/2,(ny[j]+ny[k])/2+(500-(ny[j]+ny[k])));   
                            }   
                        //}   
                        //if (edge[i][k] != 1){   
                            ev(nx[j],nx[i],ny[j],ny[i]);   
                            va = vxt;   vb = vyt;   
                            ev(nx[j],nx[k],ny[j],ny[k]);   
                            ip_check = nip(va,vxt,vb,vyt);   
                            if (ip_check < 0){   
                                g.setColor(Color.white);   
                                g.drawLine(a,b+(500-2*b),(nx[i]+nx[k])/2,(ny[i]+ny[k])/2+(500-(ny[i]+ny[k])));     
                            }   
                        //}            
                    }   
                    count=0;   
                }   
            }   
        }   
        for (int j=0;j<N;j++){   
            T.getnode(j);   
            T.drwnode();       
        }   
    }   
    public void warpping()   
    {   
        double ip, maxip = -9999.0;    
           
               
        if (count1 == 0){ // ¡ì?£¤X3¨¬¡èpy-¨¨   
            for (int i=0;i<N;i++){   
                if (ny[i]<min){   
                    min = ny[i];   
                    saveindex = i;   
                    startindex = saveindex;   
                }      
            }   
        }   
        if (count1 != 0){ // 3]visited   
            visit[saveindex] = 1;   
            count1 = 1;   
        }   
        for (int j=0;j<N;j++){   
            if (visit[j] != 1){   
                ev(nx[saveindex],nx[j],ny[saveindex],ny[j]);   
                ip = nip(vxn,vxt,vyn,vyt);   
                if (ip>maxip){   
                    maxip = ip;   
                    tmp = j;   
                }      
            }      
        }   
           
        //g.setColor(Color.red);   
        //g.drawLine(nx[saveindex],ny[saveindex]+(350-2*ny[saveindex]),nx[tmp],ny[tmp]+(350-2*ny[tmp]));   
        edge[saveindex][tmp] = 1;   
        edge[tmp][saveindex] = 1;   
        ev(nx[saveindex],nx[tmp],ny[saveindex],ny[tmp]);   
        vxn = vxt;  vyn = vyt;   
        saveindex = tmp;   
        count1++;   
           
           
           
    }   
    ///////MATH/////   
    public static double abs(int x1, int x2, int y1, int y2) //a??¡Á   
    {   
        return Math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));     
    }   
    public static void ev(int x1, int x2, int y1, int y2) // £¤?3W¡è?|V?q   
    {   
           
        vxt = (x2-x1)/abs(x1,x2,y1,y2);   
        vyt = (y2-y1)/abs(x1,x2,y1,y2);    
    }   
    public static double nip(double vx1, double vx2, double vy1, double vy2) // ¡èo?n   
    {   
        return vx1*vx2+vy1*vy2;    
    }      
/////////////////////////////////////////////////////////////////////      
    class CustomPanel extends Panel    
    {   
   
        public CustomPanel()   
        {   
               
            addMouseListener(   
                new MouseAdapter(){   
                       
                    public void mouseClicked(MouseEvent evt)   
                    {   
                        g = getGraphics();   
                        T = new Node_paint(getGraphics());   
                        mx = evt.getX();   
                        my = evt.getY();   
                        T.setnode(mx,my,N);   
                        T.getnode(N);   
                        T.drwnode();   
                        N++;   
                       
                    }      
                }      
            );     
        }   
        public void paintComponent(Graphics g)   
        {   
            super.paintComponents(g);   
                           
        }   
        public Dimension getPreferredSize()   
        {   
            return new Dimension (450,500);    
        }   
           
               
    }   
       
    class Node_paint   
    {   
        private Graphics cg;   
        private int x0, y0;    
        int index = 0;   
        Color[]frcolor = new Color[256];   
               
           
        public Node_paint(Graphics gg)   
        {   
            cg=gg;     
        }   
           
        public void setnode(int x, int y, int n)   
        {   
            index = n;   
            nx[n] = x;   
            ny[n] = 500-y;   
               
        }   
        public void getnode(int n)   
        {   
            //if (n == 0){   
            //  x0 = 280;   
            //  y0 = 70;   
            //}   
            x0 = nx[n];   
            y0 = ny[n];    
        }   
           
        public void drwnode()   
        {   
                   
            cg.setColor(Color.blue);   
               
            //getnode(index);   
            cg.fillOval(x0-5,y0-5+(500-2*y0),10,10);   
            //g.setColor(Color.white);   
            //g.drawString(str,x0-3,y0+5);     
           
        }   
     
    }   
} 