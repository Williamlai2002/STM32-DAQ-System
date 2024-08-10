#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// WAV header structure
struct header {
    char RIFF[4];
    uint32_t fileSize;
    char WAVE[4];
    char fmt[4];
    uint32_t lFormatData;
    uint16_t typeFormat;
    uint16_t num_channels;
    uint32_t sampleRate;
    uint32_t bitRate;
    uint16_t blockAlign;
    uint16_t bitsPerSample;
    char data[4];
    uint32_t dLength;
};

int main() {
    struct header wav;

    // Initialize header with 'RIFF', 'WAVE', 'fmt ', and 'data' identifiers
    memcpy(wav.RIFF, "RIFF", 4);
    memcpy(wav.WAVE, "WAVE", 4);
    memcpy(wav.fmt, "fmt ", 4);
    memcpy(wav.data, "data", 4);

    // Known values for the WAV header
    wav.lFormatData = 16;          // PCM format size of fmt sub-chunk
    wav.typeFormat = 1;            // Type of format (1 for PCM)
    wav.num_channels = 1;          // Number of channels
    wav.sampleRate = 5000;         // Sample rate
    wav.bitsPerSample = 16;        // Bits per sample
    wav.blockAlign = (wav.num_channels * wav.bitsPerSample) / 8;
    wav.bitRate = wav.sampleRate * wav.blockAlign;

    printf("Generating a WAV file with:\nSample Rate: %d\n", wav.sampleRate);

    // Open output file in binary mode to avoid issues with specific OS text mode handling
    FILE* fp = fopen("ADC_Week7/output.wav", "wb");
    if (!fp) {
        perror("Failed to open file for writing");
        return 1;
    }

    // Open input file containing ADC data
    FILE * data = fopen("ADC_Week7/adc_data.data", "r");
    if (!data) {
        perror("Failed to open data file for reading");
        fclose(fp);
        return 1;
    }

    // Calculate duration and number of samples
    int duration = 61; // seconds
    int num_samples = duration * wav.sampleRate;

    // Set data length and file size
    wav.dLength = num_samples * wav.blockAlign;
    wav.fileSize = 4 + (8 + wav.lFormatData) + (8 + wav.dLength) - 8; // Size of the "RIFF" chunk

    // Write the header
    fwrite(&wav, sizeof(wav), 1, fp);

    // Buffer to hold audio samples
    int16_t buffer;
    char line[100];

    while (fgets(line, sizeof(line), data)) {
        buffer = (int16_t)atoi(line);  // Assuming the data file contains integer values
        fwrite(&buffer, sizeof(buffer), 1, fp);
    }

    // Close files
    fclose(fp);
    fclose(data);

    printf("WAV file has been generated.\n");

    return 0;
}
