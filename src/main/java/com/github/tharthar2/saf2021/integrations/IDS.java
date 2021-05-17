package com.github.tharthar2.saf2021.integrations;

import com.github.alexthe666.citadel.server.entity.EntityPropertiesHandler;
import com.github.alexthe666.iceandfire.entity.props.FrozenEntityProperties;
import com.oblivioussp.spartanweaponry.api.WeaponMaterial;
import com.oblivioussp.spartanweaponry.api.trait.MeleeCallbackWeaponTrait;
import net.minecraft.entity.Entity;
import net.minecraft.entity.LivingEntity;
import net.minecraft.item.ItemStack;
import net.minecraft.potion.EffectInstance;
import net.minecraft.potion.Effects;

public class IDS extends MeleeCallbackWeaponTrait {

    public IDS(String propType, String propModId, TraitQuality quality) {
        super(propType, propModId, quality);
    }

    public void onHitEntity(WeaponMaterial material, ItemStack stack, LivingEntity target,
                            LivingEntity attacker, Entity projectile) {
        FrozenEntityProperties frozenProps = EntityPropertiesHandler.INSTANCE.getProperties(target, FrozenEntityProperties.class);
        frozenProps.setFrozenFor(300);
        target.addPotionEffect(new EffectInstance(Effects.SLOWNESS, 300, 2));
        target.applyKnockback( 1F, attacker.getPosX() - target.getPosX(), attacker.getPosZ() - target.getPosZ());
    }
}
