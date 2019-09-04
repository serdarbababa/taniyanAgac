using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace rakamTanima
{
    public class Spektron
    {
        //double[,,] resPixels;
        //double[,,] candidatePixels;
        //int finalBranchCount =9;
        //int candidateBranchCount = 9;
        public int windowLength ;
        public int branchLength ;
        double[,] filters;
        List<List<double>> branches;
        List<double> branchesCount;
        List<double> branchesEnery;
        double hata;

        public Spektron(int windowLen, double hata)
        {
            windowLength = Convert.ToInt32( Math.Sqrt(windowLen));
            branchLength = windowLen;
            this.hata = hata;
            //resPixels = new double [finalBranchCount, windowLength, windowLength];// pixels.GetLength(0), pixels.GetLength(1)];
            //candidatePixels = new double [candidateBranchCount, windowLength, windowLength];// pixels.GetLength(0), pixels.GetLength(1)];
            filters =  new double[4,9]{                 
                { 0, 0, 0, 0, 1, 0, 0, 0, 0 },
                { 0, 1, 0, 1, 1, 1, 0, 1, 0 },
                { 0, 1,0, 0,1,0,0,1,0},
                { 0, 0, 1, 0, 1, 0, 1, 0, 0}

            };
            branches = new List<List<double>>();
            branchesCount = new List<double>();
            branchesEnery = new List<double>();



        }

        public int learn(double[] data)
        {
            double maxSym = double.MaxValue;
            int maxSymID = -1;
            for (int i = 0; i < branches.Count; i++)
            {
                double sym = checkSym(data,i);
                if(maxSym > sym)
                {
                    maxSym = sym;
                    maxSymID = i;
                }

            }

            if (maxSymID < 0)
                return addBranch(data);
            else if (maxSym > hata)
                return addBranch(data);

            else
            {
                branchesCount[maxSymID]++;
                return maxSymID;
            }
            
        }
        public int addBranch(double []data)
        {
            List<double> temp = new List<double>() ;
            for (int i = 0; i < data.Length; i++)
                temp.Add(data[i]);
            branches.Add(temp);
            branchesCount.Add(0);
            branchesEnery.Add(0);
            return branches.Count;
        }

        public double test(double[] data)
        {
            return 0;
        }

        public double checkSym(double [] data, int branchID)
        {
            double sym = 0;
            for (int i = 0; i < data.Length; i++)
                sym += Math.Abs(data[i] - branches[branchID][i]) ;
            return sym;

        }


        public double testData(double[] data, int branchID)
        {
            double sym = 0;
            for (int b = 0; b < branches.Count; b++)
            {
                for (int i = 0; i < data.Length; i++)
                    sym += Math.Abs(data[i] - branches[branchID][i]);
            }
            return sym;

        }
        public string yazdir()
        {
            for (int i = 0; i < branches.Count; i++)
                for(int j=0;j<branches[i].Count; j++)
                    branchesEnery[i] += Math.Pow(2, (j/3)+ (j%3))* branches[i][j]  ;

            string sonuc = "";
            for (int i = 0; i < branches.Count; i++)
            {
                sonuc += "B"+i+"\tcount = " + branchesCount[i]+"\t energy= "+ String.Format("{0:0.0}", branchesEnery[i])+"\t";
                for (int j = 0; j < branches[i].Count; j++)
                    sonuc += "    " + String.Format("{0:0.0}", branches[i][j]) ; 

                sonuc += "\r\n";
            }
            return sonuc;
        }




        //public double compSymilarity(double[ ] data)
        //{
        //    double maxSym = 0;
        //    for (int brancID = 0; brancID < branches.Count; brancID++)
        //    {
        //        double sym = 0;
        //        for (int i = 0; i < data.Length; i++)
        //            sym += Math.Abs(data[i] - branches[branchID][i]);
        //    }
        //    return sym;
            
        //}


        

        public byte [,,] getFilters()
        {
            //byte[,,] res = new byte[finalBranchCount, windowLength, windowLength];
            //for (int f = 0; f < finalBranchCount; f++)
            //    for (int i = 0; i < 3; i++)
            //        for (int j = 0; j < 3; j++)
            //            res[f, i, j] = Convert.ToByte(resPixels[f, i,j]);
            //return res;
            return null;
           
        }

        public byte[,] convolve( int  imgId, int filterID)
        {
            int imgRows = Form1.images.GetLength(1);
            int fltRows = windowLength; // filter.GetLength(0);
            int imgCols = Form1.images.GetLength(2);
            int fltCols =  windowLength;// filter.GetLength(1);

            int halfFilter = Convert.ToInt16(fltCols / 2);

            byte[,] result = new byte[imgRows - 2 * halfFilter, imgCols-2*halfFilter];


            //Parallel.For(0, imgRows - 2*halfFilter, i =>
            for (int i =0;i< imgRows - 2 * halfFilter;i++)
            {
                for (int j = 0; j < imgCols - 2*halfFilter; j++)
                {
                    double temp = 0;
                    double sum = 0;
                    for (int k = 0; k < fltCols; k++)
                    {
                        for (int l = 0; l < fltCols; l++)
                        {
                            temp += Form1.images[imgId, i + k, j + l] * filters[filterID, k * windowLength + l];
                            sum+= filters[filterID, k * windowLength + l];
                        }
                    }
                    temp = temp / sum;
                    if (temp > 255)
                        temp = 255;
                    else if (temp < 0)
                        temp = 0;
                    

                    result[i, j] = Convert.ToByte(temp);
                }
            }//); // Parallel.For
            return result;

        }
    }
}
