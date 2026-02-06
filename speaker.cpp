#include <iostream>
#include <windows.h>
#include <sapi.h>

using namespace std;

int main() 
{
    ISpVoice *pVoice = NULL;
    if (FAILED(::CoInitialize(NULL))) return FALSE;

    HRESULT hr = CoCreateInstance(CLSID_SpVoice, NULL, CLSCTX_ALL, IID_ISpVoice, (void **)&pVoice);
    if (SUCCEEDED(hr)) {
        string input;
        getline(cin, input);
        wstring wide_input(input.begin(), input.end());
        pVoice->Speak(wide_input.c_str(), 0, NULL);
        pVoice->Release();
    }
    ::CoUninitialize();
    return TRUE;
}


