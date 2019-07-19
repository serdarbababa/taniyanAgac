using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace rakamTanima
{
    public class GaborKernel
    {
        public GaborKernel()
        {

        }
        public float[,] getGaborKernel(int _width, double lambda, double theta, double psi, double sigma, double gamma) 
        {
            int width = _width;


            float[,] real = new float[width, width];
            //real = new Matrix<float>(width, width);

            for (int i = 0; i < width; i++)
            {
                for (int j = 0; j < width; j++)
                {
                    int x = i - width / 2;
                    int y = j - width / 2;

                    double x_prime = x * Math.Cos(theta) + y * Math.Sin(theta);
                    double y_prime = -x * Math.Sin(theta) + y * Math.Cos(theta);

                    double a = Math.Exp(-(x_prime * x_prime + gamma * gamma * y_prime * y_prime) / (2 * sigma * sigma));
                    double re = Math.Cos(2 * Math.PI * x_prime / lambda + psi);
                    double im = Math.Sin(2 * Math.PI * x_prime / lambda + psi);//*/

                    double real_part = a * re;
                    double imaginary_part = a * im;

                    real[i, j] = (float)real_part;
                    //imaginary.Data[i, j] = (float)imaginary_part;
                }
            }
            return real;
        }

        public void useClass()
        {
            int counter = 0;
            double psi = 2;// phase offset
            double gamma = 1;// Aspect ratio of the Gaussian curves
            double theta = (counter % 17) * Math.PI / 8;// orientation
            double sigma = 5; // Sigma defining the size of the Gaussian envelope = 8 //Gaussian variance
            double lambda = 5; //wavelength
            int width = 20;
            counter = counter + 1;






            float[,] g = new GaborKernel().getGaborKernel(width, lambda, theta, psi, sigma, gamma);

            int zoomFactor = 3;// Convert.ToInt32(txtZoom.Text);
            System.Drawing.Bitmap bmp = new Bitmap(width * zoomFactor, width * zoomFactor);

            for (int i = 0; i < width; ++i)
            {
                for (int j = 0; j < width; ++j)
                {
                    byte b = Convert.ToByte(100 * (g[i, j] + 1));
                    for (int k = 0; k < zoomFactor; k++)
                        for (int l = 0; l < zoomFactor; l++)
                            bmp.SetPixel(j * zoomFactor + k, i * zoomFactor + l, Color.FromArgb(b, b, b));
                }
            }

            //pictureBox1.Image = (Image)bmp;

            //pictureBox1.Show();
        }

    }

}
