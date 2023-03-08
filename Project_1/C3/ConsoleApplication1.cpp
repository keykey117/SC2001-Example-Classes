#include <iostream>
#include <vector>
#include <cstdlib>
#include <math.h>
#include <time.h>
#include <fstream>
#include <chrono>
#include <string>

int count = 0;

std::vector<std::vector<int>> generateData(int min, int max, int x) {
    std::vector<std::vector<int>> outerData;
    int size = min;
    while (size <= max) {
        std::cout << "Generating ...\n";
        std::vector<int>innerData;
        innerData.reserve(size);
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
    for (int i = 1; i < data.size();i++) {
        for (int j = i; j > 0; j--) {
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
    result.reserve(lVec.size()+rVec.size());
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
        //insertionSort(data);
        //return data;
    }
    int midPoint = data.size() / 2;
    std::vector <int> lVec= hybridSort(std::vector<int>(data.begin(), data.begin() + midPoint), S);
    std::vector <int> rVec = hybridSort(std::vector<int>(data.begin() + midPoint, data.end()), S);
    std::vector <int> result = merge(lVec, rVec);
    return result;

}

std::vector <int> mergeSort(std::vector <int> data) {
    if (data.size() <= 1) {
        return data;
    }
    else {
        int midPoint = data.size() / 2;
        std::vector <int> lVec = std::vector<int>(data.begin(), data.begin() + midPoint);
        std::vector <int> rVec = std::vector<int>(data.begin() + midPoint, data.end());
        lVec = mergeSort(lVec);
        rVec = mergeSort(rVec);
        return merge(lVec, rVec);
    }
}

void print(std::vector <int> & a) {
    std::cout << "\nThe vector elements are : ";
    for (int i = 0; i < a.size(); i++)
        std::cout << a.at(i) << ' ';
}

void printVecVec(std::vector<std::vector<int>> & a) {
    std::cout << "The vector elements are : ";
    for (int i = 0; i < a.size(); i++) {
        std::cout << "\n For" << i;
        for (int j = 0; j < a[i].size(); j++) {
            std::cout << a[i].at(j) << ' ';
        }
        std::cout << "Size is " << a[i].size();
    }
}


void c3() {
    std::vector<std::vector<int>>data = generateData(1, pow(10, 7), 1000);
    //printVecVec(generateData(1, 100, 5));

    double bestSRunTime = 0;
    double bestRunTime = 1000000000000;
    double bestSKeyComp = 0;
    double bestKeyComp = pow(10, 10);
    std::vector <int> resultsRunTime;
    resultsRunTime.reserve(100);

    std::vector <int> resultsKeyComp;
    resultsKeyComp.reserve(100);

    for (int S = 1; S < 100 + 1; S++) {
        count = 0;
        auto start = std::chrono::high_resolution_clock::now();
        std::vector <int> res = hybridSort(data[5], S);
        //print(res);
        auto end = std::chrono::high_resolution_clock::now();
        double runTime = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
        resultsRunTime.push_back(runTime);
        resultsKeyComp.push_back(count);
        if (runTime < bestRunTime) {
            bestRunTime = runTime;
            bestSRunTime = S;
        }
        if (count < bestKeyComp) {
            bestKeyComp = count;
            bestSKeyComp = S;
        }
    }
    std::cout << "\nS for best runtime: " << bestSRunTime << "\t Elapsed time: " << bestRunTime;
    std::cout << "\nS for key comparisons: " << bestSKeyComp << "\t Num of Key Comparisons: " << bestKeyComp;

    std::fstream fileRT;
    fileRT.open("resultsRunTime5_new.txt", std::ios_base::out);
    for (int i = 0;i < resultsRunTime.size();i++)
    {
        fileRT << resultsRunTime[i] << std::endl;
    }
    fileRT.close();

    std::fstream fileKC;
    fileKC.open("resultsKeyComp5_new.txt", std::ios_base::out);
    for (int i = 0;i < resultsKeyComp.size();i++)
    {
        fileKC << resultsKeyComp[i] << std::endl;
    }
    fileKC.close();
}

void d() {
    std::vector<std::vector<int>>data = generateData(1, pow(10, 7), 1000);
    count = 0;
    auto start = std::chrono::high_resolution_clock::now();
    mergeSort(data[7]);
    auto end = std::chrono::high_resolution_clock::now();
    double runTime = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
    std::cout<< "runtime for merge sort is " << runTime;
    std::cout << "\nkey comparisons for merge sort is " << count;

    count = 0;
    start = std::chrono::high_resolution_clock::now();
    hybridSort(data[7],10);
    end = std::chrono::high_resolution_clock::now();
    runTime = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
    std::cout << "\nruntime for hybrid sort is " << runTime;
    std::cout << "\nkey comparisons for hybrid sort is " << count;

    
}
int main()
{
    c3();
    //d();

}