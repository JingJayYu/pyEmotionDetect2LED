#include <FastLED.h>
#define NUM_LEDS 8
#define LED 7

#define LED_PIN     7
#define NUM_LEDS    8
#define BRIGHTNESS  5
#define LED_TYPE    WS2812B
#define COLOR_ORDER GRB
CRGB leds[NUM_LEDS];
CRGBPalette16 currentPalette;
TBlendType    currentBlending;

#define UPDATES_PER_SECOND 100

byte ignite_num = 0;


void setup() {
    Serial.begin(9600);
    FastLED.addLeds<LED_TYPE, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS).setCorrection( TypicalLEDStrip );
    FastLED.setBrightness(  BRIGHTNESS );
    currentPalette = RainbowColors_p;
    currentBlending = LINEARBLEND;
}

void all_LED_OUT(){
    for(int i = 0; i < NUM_LEDS; i++){
        leds[i] = CRGB::Black;
    }
}

void FillLEDsFromPaletteColors( uint8_t colorIndex, int led_num)
{
    uint8_t brightness = 255;
    
    for( int i = 0; i < led_num; ++i) {
        leds[i] = ColorFromPalette( currentPalette, colorIndex, brightness, currentBlending);
        colorIndex += 3;
    }
}

void loop() {
    static uint8_t startIndex = 0;
    startIndex = startIndex + 1; /* motion speed */

    if (Serial.available()) {
        ignite_num = Serial.read();
        Serial.println(ignite_num);
        all_LED_OUT();
    }
    FillLEDsFromPaletteColors(startIndex, ignite_num);  
    FastLED.show();
    FastLED.delay(1000 / UPDATES_PER_SECOND);
}