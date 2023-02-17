#include <iostream>
#include <vector>
#include <cstdlib>
#include <math.h>
#include <time.h>
#include <fstream>

int count = 0;

std::vector<std::vector<int>> generateData(int min, int max, int x) {
    std::vector<std::vector<int>> outerData;
    int size = min;
    while (size <= max) {
        std::cout << "Generating ...\n";
        std::vector<int>innerData;
        for (int i = 0; i < size;i++) {
            innerData.push_back(rand() % x);
        }
        outerData.push_back(innerData);
        size *= 10;
    }
    return outerData;
}

std::vector <int> insertionSort(std::vector<int> data) {
    int temp = 0;
    for (int i = 1; i<data.size();i++) {
        for (int j = i; j >0; j--) {
            count++;
            if (data[j] < data[j - 1]) {
                temp = data[j];
                data[j] = data[j - 1];
                data[j - 1] = temp;
            }
        }
    }
    return data;
}

std::vector <int> merge(std::vector<int> lVec, std::vector<int> rVec) {
    int i = 0;
    int j = 0;
    std::vector<int> result;
    while (i <= lVec.size() - 1 and j <= rVec.size() - 1) {
        count++;
        if (lVec[i] < rVec[j]) {
            result.push_back(lVec[i]);
            i++;
        }
        else {
            result.push_back(rVec[j]);
            j++;
        }
    }
    if (i != lVec.size()) {
        result.insert(result.end(), lVec.begin()+i, lVec.end());
    }
    else {
        result.insert(result.end(), rVec.begin() + j, rVec.end());
    }
    return result;
}

std::vector <int> hybridSort(std::vector<int> data, int S) {
    if (data.size() <= S) {
        return insertionSort(data);
    }
    int midPoint = data.size() / 2;
    std::vector <int> lVec= std::vector<int>(data.begin(), data.begin()+midPoint);
    std::vector <int> rVec = std::vector<int>(data.begin()+midPoint, data.end());
    lVec = hybridSort(lVec, S);
    rVec = hybridSort(rVec, S);
    std::vector <int> result = merge(lVec, rVec);
    return result;

}

void print(std::vector <int> const& a) {
    std::cout << "The vector elements are : ";
    for (int i = 0; i < a.size(); i++)
        std::cout << a.at(i) << ' ';
}

void printVecVec(std::vector<std::vector<int>> const& a) {
    std::cout << "The vector elements are : ";
    for (int i = 0; i < a.size(); i++) {
        std::cout << "\n For" << i;
        for (int j = 0; j < a[i].size(); j++) {
            std::cout << a[i].at(j) << ' ';
        }
        std::cout << "Size is " << a[i].size();
    }
}

int main()
{
    std::vector<std::vector<int>>data = generateData(1, pow(10, 7), 1000);
    //printVecVec(generateData(1, 100, 5));
    time_t start, end;

    double bestSRunTime = 0;
    double bestRunTime = 1000000;

    double bestSKeyComp = 0;
    double bestKeyComp = pow(10,10);

    for (int S = 1; S < 10+1; S++) {
        count = 0;
        std::cout << S << "\n";
        time(&start);
        hybridSort(data[7], S);
        time(&end);
        double runTime = difftime(end, start);
        if (runTime < bestRunTime) {
            bestRunTime = runTime;
            bestSRunTime = S;
        }
        if (count < bestKeyComp) {
            bestKeyComp = count;
            bestSKeyComp = S;
        }
    }
    //std::vector <int> res= hybridSort(data[7], 4);
    //print(res);
    std::cout << "\nS for best runtime: " << bestSRunTime << "\t Elapsed time: " << bestRunTime;
    std::cout << "\nS for key comparisons: " << bestSKeyComp << "\t Num of Key Comparisons: " << bestKeyComp;
}